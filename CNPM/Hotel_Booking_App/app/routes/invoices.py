from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection
from decimal import Decimal
from app.utils import get_userid_from_token, get_hotel_id_from_room_id
import mysql.connector as connect

invoices_bp = Blueprint("invoices", __name__)

@invoices_bp.route("/invoices", methods=["POST"])
@jwt_required()
def create_invoices():
    data = request.json
    print(data)
    customer_id = get_userid_from_token()
    print(customer_id)
    room_type_id = data.get("room_type_id")
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    additional_services = data.get("additional_services", [])
    forwho = data.get("forwho", False)
    anothercustomer = data.get("anothercustomer")
    anotherccid = data.get("anotherccid")

    hotel_id = get_hotel_id_from_room_id(room_type_id)

    if not all([customer_id, room_type_id, check_in, check_out, hotel_id]):
        return jsonify({"error": "Thiếu thông tin đặt phòng"}), 400

    if check_in >= check_out:
        return jsonify({"error": "Ngày check-in phải trước ngày check-out"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Lấy giá phòng
        cursor.execute("SELECT price, availability FROM roomtypes WHERE id = %s", (room_type_id,))
        room_info = cursor.fetchone()
        if not room_info:
            return jsonify({"error": "Loại phòng không hợp lệ"}), 400

        room_price, availability = room_info
        if availability <= 0:
            return jsonify({"error": "Loại phòng đã hết chỗ"}), 400

        # Lấy mức giảm giá khách hàng
        cursor.execute("""
            SELECT d.discount FROM customers c
            JOIN discounts d ON c.customer_type = d.id
            WHERE c.id = %s
        """, (customer_id,))
        discount = cursor.fetchone()
        discount = float(discount[0]) if discount else 0

        # Tính giá dịch vụ bổ sung
        total_service_price = 0
        service_ids = []
        if additional_services:
            if isinstance(additional_services, str):
                additional_services = [s.strip() for s in additional_services.split(',')]

            cursor.execute(
                "SELECT id, price FROM additionalservices WHERE service_name IN (%s)" %
                ','.join(['%s'] * len(additional_services)),
                tuple(additional_services)
            )
            services = cursor.fetchall()
            service_ids = [row[0] for row in services]
            total_service_price = sum(row[1] for row in services)

        # Tổng tiền
        total_price = Decimal(room_price + total_service_price)
        total_price -= (Decimal(discount) / 100) * total_price

        # Insert hóa đơn
        cursor.execute("""
            INSERT INTO invoices (
                customer_id, room_type_id, check_in, check_out, total_price, hotel_id,
                is_for_someone_else, other_person_name, other_person_ccid
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            customer_id, room_type_id, check_in, check_out, total_price, hotel_id,
            forwho, anothercustomer if forwho else None, anotherccid if forwho else None
        ))
        invoice_id = cursor.lastrowid

        # Gán dịch vụ bổ sung
        for service_id in service_ids:
            cursor.execute("""
                INSERT INTO invoice_additionalservices (invoice_id, service_id)
                VALUES (%s, %s)
            """, (invoice_id, service_id))

        # Trừ số lượng phòng còn lại
        cursor.execute("""
            UPDATE roomtypes SET availability = availability - 1 WHERE id = %s
        """, (room_type_id,))

        conn.commit()
        return jsonify({
            "message": "Đặt phòng thành công",
            "invoice_id": invoice_id,
            "total_price": float(total_price)
        }), 201

    except connect.Error as err:
        conn.rollback()
        return jsonify({"error": str(err)}), 500

    finally:
        cursor.close()
        conn.close()
@invoices_bp.route("/invoices/<int:invoices_id>",methods=["UPDATE"])
@jwt_required()
def updated_invoicess(invoices_id):
    data = request.json
    if not data:
        return jsonify({"message": "Không có data!"})
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    additional_services = data.get("additional_services")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if check_in and check_out:
            cursor.execute(
                "UPDATE invoices SET check_in = %s, check_out = %s WHERE id = %s",
                (check_in, check_out, invoices_id),
            )
        cursor.execute("DELETE FROM invoice_additionalservices WHERE invoice_id = %s", (invoices_id,))
        if additional_services:
            for service_id in additional_services:
                cursor.execute(
                    "INSERT INTO invoice_additionalservices (invoice_id, service_id) VALUES (%s, %s)",
                    (invoices_id, service_id),
                )
        conn.commit()
        return jsonify({"message": "Hóa đơn cập nhật thành công"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()
@invoices_bp.route("/invoices/<int:invoices_id>",methods=["DELETE"])
@jwt_required()
def delete_invoices(invoices_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM invoices WHERE id = %s",(invoices_id, ))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Invoices deleted successfully"}), 201

    