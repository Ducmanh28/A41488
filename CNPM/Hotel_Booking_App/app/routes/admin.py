from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from utils import get_db_connection

admin_bp = Blueprint("admin",__name__)

@admin_bp.route("/admin/customers/total",methods=["GET"])
@jwt_required()
def get_total_customers():
    count = 0
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id from customers where role = 'customers' ")
    customers = cursor.fetchall()
    for customer in customers:
        count += 1
    return count
@admin_bp.route("/admin/customers",methods=["GET"])
@jwt_required()
def get_all_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)
@admin_bp.route("/admin/customers/<int:customer_id>",methods=["DELETE"])
@jwt_required()
def remove_customers(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE * FROM customers WHERE id = %s",(customer_id, ))
    conn.commit
    cursor.close()
    conn.close()
    return jsonify({"message": "Xóa user thành công!"})
@admin_bp.route("/admin/customers/<int:customer_id>",methods=["PUT"])
@jwt_required()
def updated_customers(customer_id):
    data = request.json
    if not data:
        return jsonify({"error": "Dữ liệu cập nhật không hợp lệ"}), 400

    fields = []
    values = []

    # Duyệt qua các trường dữ liệu
    if "username" in data:
        fields.append("username = %s")
        values.append(data["username"])
    if "phone" in data:
        fields.append("phone_number = %s")
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
    values.append(customer_id)
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
@admin_bp.route("/admin/customers/create_user",methods=["POST"])
@jwt_required()
def create_customers():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")  
    phone = data.get("phone_number")
    full_name = data.get("full_name") 
    citizen_id = data.get("citizen_id")
    role = data.get("role")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers(username,email,password,phone_number,full_name,citizen_id,role) VALUES(%s,%s,%s,%s,%s,%s,%s)",(username,email,password,phone,citizen_id,full_name,role))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Tạo thành công!"})