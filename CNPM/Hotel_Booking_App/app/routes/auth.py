from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import mysql.connector as connect
from db import get_db_connection
from datetime import timedelta
import random
from app.utils import get_db_connection,get_old_passwords,send_email,is_new_password_valid,is_valid_password
from time import time

otp_storage = {}
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")  
    phone = data.get("phone_number")
    otp_code = data.get("otp") 
    full_name = data.get("full_name") 
    citizen_id = data.get("citizen_id")

    if not is_valid_password(password):
        return jsonify({"error": "Mật khẩu phải trên 8 kí tự và chứa ít nhất 1 kí tự đặc biệt!"}),400
    # Kiểm tra thông tin đầu vào
    if not username or not email or not password or not phone or not full_name or not citizen_id:
        return jsonify({"error": "Vui lòng nhập đầy đủ thông tin trước khi đăng ký!"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
    user = cursor.fetchone()

    # Nếu có OTP -> Xác thực OTP
    if otp_code:
        if email not in otp_storage:
            return jsonify({"error": "Email chưa yêu cầu OTP hoặc OTP đã hết hạn!"}), 400

        stored_data = otp_storage[email]
        if stored_data["expires"] < time():
            del otp_storage[email]
            return jsonify({"error": "OTP đã hết hạn, vui lòng thử lại!"}), 400

        if stored_data["otp"] != otp_code:
            return jsonify({"error": "OTP không chính xác!"}), 400

        # OTP hợp lệ -> Thêm user vào database (KHÔNG HASH PASSWORD)
        try:
            cursor.execute("INSERT INTO customers (username, email, phone_number, password, citizen_id, full_name) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (username, email, phone, password,citizen_id, full_name))
            conn.commit()
            cursor.close()
            conn.close()
            del otp_storage[email]  # Xóa OTP sau khi xác nhận thành công
            return jsonify({"message": "Đăng ký thành công!"}), 201
        except connect.Error as err:
            return jsonify({"error": str(err)}), 500

    # Nếu không có OTP -> Gửi OTP
    if user:
        return jsonify({"error": "Email đã được sử dụng!"}), 400

    otp_code = str(random.randint(100000, 999999))
    otp_storage[email] = {"otp": otp_code, "expires": time() + 300}

    if send_email(email, otp_code):
        return jsonify({"message": "Mã OTP đã được gửi đến email!"}), 200
    else:
        return jsonify({"error": "Không thể gửi email!"}), 500
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data:
        return jsonify({"error": "Request body phải là JSON"}), 400
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if (username and email) or (not username and not email):
        return jsonify({"error": "Bạn phải nhập username hoặc email, không được nhập cả hai hoặc bỏ trống"}), 400

    identifier = username if username else email  
    field = "username" if username else "email"  

    if not password:
        return jsonify({"error": "Password không được để trống"}), 400
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"SELECT username, password, id FROM customers WHERE {field} = %s"
        cursor.execute(query, (identifier,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and user[1] == password:
            access_token = create_access_token(identity=user[0],expires_delta=timedelta(hours=1))
            return jsonify({"message": "Đăng nhập thành công", "access_token": access_token, "customer_id": user[2]}), 200
        else:
            return jsonify({"error": "Sai username/email hoặc password"}), 401

    except connect.Error as err:
        return jsonify({"error": str(err)}), 500  
@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.json
    email = data.get("email")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()

    if not user:
        return jsonify({"error": "Email không tồn tại"}), 400

    # Tạo OTP ngẫu nhiên
    otp_code = str(random.randint(100000, 999999))

    # Lưu OTP vào bộ nhớ tạm
    otp_storage[email] = {"otp": otp_code, "expires": time() + 300}
    if send_email(email, otp_code):
        return jsonify({"message": "Mã OTP đã được gửi đến email"}), 200
    else:
        return jsonify({"error": "Không thể gửi email!"}), 500
@auth_bp.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.json
    email = data.get("email")
    otp_code = data.get("otp")
    new_password = data.get("new_password")
    old_passwords = get_old_passwords(email)
    if not is_new_password_valid(new_password, old_passwords):
        return {"error": "Mật khẩu mới không được trùng với 3 lần gần nhất"}
    if not email or not otp_code or not new_password:
        return jsonify({"error": "Email, OTP và mật khẩu mới không được để trống"}), 400

    # Kiểm tra OTP
    if email not in otp_storage or otp_storage[email]["otp"] != otp_code:
        return jsonify({"error": "Mã OTP không hợp lệ hoặc đã hết hạn"}), 400

    # Cập nhật mật khẩu
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    UPDATE customers 
    SET 
        password = %s, 
        old_password_3 = old_password_2, 
        old_password_2 = old_password_1, 
        old_password_1 = %s
    WHERE email = %s;
    """
    cursor.execute(query, (new_password, old_passwords[0], email))
    conn.commit()
    cursor.close()
    conn.close()

    # Xóa OTP sau khi sử dụng
    del otp_storage[email]

    return jsonify({"message": "Đặt lại mật khẩu thành công"}), 200
