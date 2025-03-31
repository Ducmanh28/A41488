from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection
from decimal import Decimal
import mysql.connector as connect

invoices_bp = Blueprint("invoices", __name__)

@invoices_bp.route("/invoices", methods=["POST"])
@jwt_required()
def create_invoices():
    data = request.json
    customer_id = data.get("customer_id")
    room_type_id = data.get("room_type_id")
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    additional_services = data.get("additional_services", [])  
    hotel_id = data.get("hotel_id")

    if not all([customer_id, room_type_id, check_in, check_out, hotel_id]):
        return jsonify({"error": "Thiếu thông tin đặt phòng"}), 400
    if check_in >= check_out:
        return jsonify({"error": "Ngày check-in phải trước ngày check-out"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # 📌 Lấy giá phòng từ bảng roomtypes
        cursor.execute("SELECT price FROM roomtypes WHERE id = %s", (room_type_id,))
        room_price = cursor.fetchone()
        if not room_price:
            return jsonify({"error": "Loại phòng không hợp lệ"}), 400
        room_price = room_price[0]

        # 📌 Lấy discount từ bảng discounts (dựa trên customer_id)
        cursor.execute("""
            SELECT d.discount FROM customers c
            JOIN discounts d ON c.customer_type = d.id
            WHERE c.id = %s
        """, (customer_id,))
        discount = cursor.fetchone()
        discount = discount[0] if discount else 0

        # 📌 Lấy tổng giá của các dịch vụ bổ sung
        total_service_price = 0
        service_ids = []
        if additional_services:
            additional_services = [service.strip() for service in additional_services.split(',')]
            cursor.execute("SELECT id, price FROM additionalservices WHERE service_name IN (%s)" % 
                           ','.join(['%s'] * len(additional_services)), tuple(additional_services))
            services = cursor.fetchall()
            service_ids = [row[0] for row in services]
            total_service_price = sum(row[1] for row in services)

        # 📌 Tính total_price
        discount = float(discount) if discount else 0
        total_prices = (room_price + total_service_price)
        total_prices = Decimal(total_prices)
        total_price = total_prices - ((Decimal(discount) / Decimal(100)) * total_prices)


        # 📌 Thêm invoice mới
        cursor.execute(
            "INSERT INTO invoices (customer_id, room_type_id, check_in, check_out, total_price, hotel_id) VALUES (%s, %s, %s, %s, %s, %s)", 
            (customer_id, room_type_id, check_in, check_out, total_price, hotel_id)
        )
        invoice_id = cursor.lastrowid  

        # 📌 Chèn vào bảng invoice_additionalservices nếu có dịch vụ bổ sung
        for service_id in service_ids:
            cursor.execute("INSERT INTO invoice_additionalservices (invoice_id, service_id) VALUES (%s, %s)", 
                           (invoice_id, service_id))

        conn.commit()
        return jsonify({"message": "Đặt phòng thành công", "invoice_id": invoice_id, "total_price": total_price}), 201

    except connect.Error as err:
        conn.rollback()
        return jsonify({"error": str(err)}), 500

    finally:
        cursor.close()
        conn.close()

@invoices_bp.route("/invoices", methods=["GET"])
@jwt_required()
def get_invoicess():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM invoicess")
    invoicess = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(invoicess)
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
    
    return jsonify({"message": "invoices deleted successfully"}), 201