from db import get_db_connection
from flask import Blueprint, request, jsonify
customers_bp = Blueprint("customers", __name__)


@customers_bp.route("/customers",methods=["GET"])
def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)
@customers_bp.route("/customers/<int:user_id>",methods=["GET"])
def get_users(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers WHERE id = %s",(user_id, ))
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)
@customers_bp.route("/customers/<int:user_id>",methods=["PUT"])
def updated_users(user_id):
    data = request.json
    if not data:
        return jsonify({"error": "Dữ liệu cập nhật không hợp lệ"}), 400

    fields = []
    values = []

    # Duyệt qua các trường dữ liệu
    if "username" in data:
        fields.append("customername = %s")
        values.append(data["username"])
    if "phone" in data:
        fields.append("phone = %s")
        values.append(data["phone"])
    if "email" in data:
        fields.append("email = %s")
        values.append(data["email"])
    if "password" in data:
        fields.append("password = %s")
        values.append(data["password"])
    if "full_name" in data:
        fields.append("full_name = %s")
        values.append(data["full_name"])
    if "birth_date" in data:
        fields.append("birth_date = %s")
        values.append(data["birth_date"])
    if "current_address" in data:
        fields.append("current_address = %s")
        values.append(data["current_address"])

    # Nếu không có trường nào để cập nhật, trả về lỗi
    if not fields:
        return jsonify({"error": "Không có thông tin nào để cập nhật"}), 400

    # Ghép câu lệnh SQL
    query = f"UPDATE customers SET {', '.join(fields)} WHERE id = %s"
    values.append(user_id)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@customers_bp.route("/customers/<int:user_id>",methods=["DELETE"])
def deleted_users(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = %s", (user_id, ))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "User deleted successfully"}), 201