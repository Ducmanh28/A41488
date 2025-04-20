from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection
from decimal import Decimal
from app.utils import get_userid_from_token, get_hotel_id_from_room_id, get_service_id, format_rfc1123_to_date
from datetime import datetime
import mysql.connector as connect

invoices_bp = Blueprint("invoices", __name__)

@invoices_bp.route("/invoices", methods=["POST"])
@jwt_required()
def create_invoices():
    data = request.json
    customer_id = get_userid_from_token()
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
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        print(check_in_date,check_out_date)
        if not check_in_date:
            print("Không có giá trị check_in_date")
        num_nights = (check_out_date - check_in_date).days
        print(num_nights)
        # Tổng tiền
        total_price = Decimal(room_price*num_nights + total_service_price)
        print(total_price)
        total_price -= (Decimal(discount) / 100) * total_price
        cursor.execute("SELECT room_number FROM busy_room WHERE hotel_id=%s AND room_type_id=%s AND state='Free'",(hotel_id,room_type_id))
        rooms = cursor.fetchall()
        room = rooms[0][0]
        # Insert hóa đơn
        cursor.execute("""
            INSERT INTO invoices (
                customer_id, room_type_id, check_in, check_out, total_price, hotel_id,
                is_for_someone_else, other_person_name, other_person_ccid,room_number
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """, (
            customer_id, room_type_id, check_in, check_out, total_price, hotel_id,
            forwho, anothercustomer if forwho else None, anotherccid if forwho else None,room
        ))
        invoice_id = cursor.lastrowid
        cursor.execute("UPDATE busy_room SET state='Busy',busy_from=%s,busy_to=%s,invoice_id=%s WHERE hotel_id=%s AND room_type_id=%s AND room_number=%s",(check_in_date,check_out_date,invoice_id,hotel_id,room_type_id,room))
        conn.commit()
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
        action = "CREATE INVOICE"
        cursor.execute("INSERT INTO log(customer_id,action) VALUES(%s,%s)",(customer_id,action))
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
@invoices_bp.route("/invoices/<int:invoices_id>",methods=["PUT"])
@jwt_required()
def updated_invoicess(invoices_id):
    data = request.json
    
    if not data:
        return jsonify({"message": "Không có data!"}), 400

    check_in = data.get("check_in")
    check_out = data.get("check_out")
    additional_services = data.get("additional_services", [])
    state = data.get("state")
    
    try:
        total = Decimal(str(data.get("total_price")))
    except:
        return jsonify({"message": "total_price không hợp lệ!"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)
    
    try:
        new_total = total
        new_state = state

        if state == "DA THANH TOAN":
            cursor.execute("SELECT total_money FROM payment WHERE invoices_id = %s", (invoices_id,))
            result = cursor.fetchone()
            if not result:
                return jsonify({"message": "Không tìm thấy thanh toán trước đó"}), 404

            old_total = result[0]
            if total > old_total:
                new_total = total - old_total
                new_state = "CHUA THANH TOAN"
                message = f"Cập nhật thành công hóa đơn, Bạn còn thiếu: {new_total}!"
            elif total < old_total:
                new_total = old_total - total
                message = f"Cập nhật thành công hóa đơn, Bạn còn thừa: {new_total}!"
        elif state == "CHUA THANH TOAN":
            message = f"Cập nhật thành công hóa đơn, Vui lòng thanh toán: {new_total}!"
        # Cập nhật hóa đơn
        cursor.execute(
            "UPDATE invoices SET check_in = %s, check_out = %s, total_price = %s, state = %s WHERE id = %s",
            (check_in, check_out, new_total, new_state, invoices_id)
        )

        # Cập nhật dịch vụ đi kèm
        cursor.execute("DELETE FROM invoice_additionalservices WHERE invoice_id = %s", (invoices_id,))
        
        for service_name in additional_services:
            service_id = get_service_id(service_name)
            if service_id:
                cursor.execute(
                    "INSERT INTO invoice_additionalservices (invoice_id, service_id) VALUES (%s, %s)",
                    (invoices_id, service_id)
                )

        conn.commit()
        return jsonify({"message": message}), 200

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
@invoices_bp.route("/invoices/<int:invoices_id>",methods=["GET"])
@jwt_required()
def get_invoices_by_id(invoices_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM invoices WHERE id = %s",(invoices_id, ))
    data = cursor.fetchone()
    data["check_in"] = format_rfc1123_to_date(data["check_in"])
    data["check_out"] = format_rfc1123_to_date(data["check_out"])
    cursor.close()
    conn.close()
    return jsonify(data)
@invoices_bp.route("/invoices/<int:invoices_id>/additionalservices", methods=["GET"])
@jwt_required()
def get_additionalservice_of_invoices(invoices_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT service_id FROM invoice_additionalservices WHERE invoice_id = %s", (invoices_id,))
    services_id = cursor.fetchall()

    list_service = []
    for service_id in services_id:
        cursor.execute("SELECT service_name, price FROM additionalservices WHERE id = %s", (service_id["service_id"],))
        service = cursor.fetchone()
        if service:
            list_service.append({
                "service_id": service_id["service_id"],
                "service_name": service["service_name"],
                "service_price": service["price"]
            })
    cursor.close()
    conn.close()
    return jsonify(list_service)
        
    
    
    