from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection
import mysql.connector as connect

invoices_bp = Blueprint("invoices", __name__)

@invoices_bp.route("/invoicess", methods=["POST"])
@jwt_required()
def create_invoices():
    data = request.json
    user_id = data.get("user_id")
    room_id = data.get("room_type_id")
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    additional_services = data.get("additional_services", [])  # Mặc định là danh sách rỗng
    total_price = data.get("total_price")

    if not all([user_id, room_id, check_in, check_out, total_price]):
        return jsonify({"error": "Thiếu thông tin đặt phòng"}), 400
    if check_in >= check_out:
        return jsonify({"error": "Ngày check-in phải trước ngày check-out"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # **Thêm invoices mới**
        cursor.execute(
            "INSERT INTO invoices (user_id, room_type_id, check_in, check_out, total_price) VALUES (%s, %s, %s, %s, %s)", 
            (user_id, room_id, check_in, check_out, total_price)
        )
        invoice_id = cursor.lastrowid  # **Lấy ID của invoice vừa tạo**

        # **Lấy ID của các dịch vụ thêm**
        if additional_services:
            cursor.execute("SELECT id FROM additionalservices WHERE service_name IN (%s)" % 
                           ','.join(['%s'] * len(additional_services)), tuple(additional_services))
            service_ids = [row[0] for row in cursor.fetchall()]

            # **Chèn vào bảng invoice_additionalservices**
            for service_id in service_ids:
                cursor.execute("INSERT INTO invoice_additionalservices (invoice_id, service_id) VALUES (%s, %s)", 
                               (invoice_id, service_id))

        conn.commit()
        return jsonify({"message": "Đặt phòng thành công", "invoice_id": invoice_id}), 201

    except connect.Error as err:
        conn.rollback()
        return jsonify({"error": str(err)}), 500

    finally:
        cursor.close()
        conn.close()
@invoices_bp.route("/invoicess", methods=["GET"])
@jwt_required()
def get_invoicess():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM invoicess")
    invoicess = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(invoicess)
@invoices_bp.route("/invoicess/<int:invoices_id>",methods=["UPDATE"])
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
@invoices_bp.route("/invoicess/<int:invoices_id>",methods=["DELETE"])
@jwt_required()
def delete_invoices(invoices_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE * FROM invoicess WHERE id = %s",(invoices_id, ))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "invoices deleted successfully"}), 201