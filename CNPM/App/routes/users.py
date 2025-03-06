from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from db import get_db_connection
import random
import smtplib
import ssl
from email.message import EmailMessage
from time import time
import re
import config
otp_storage = {}
users_bp = Blueprint("users", __name__)
def get_user_from_token(token):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT users.* FROM users INNER JOIN tokens ON users.id = tokens.user_id WHERE tokens.access_token = %s"
    cursor.execute(query, (token,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return user

def send_email(receiver_email, otp_code):
    try:
        subject = "Mã OTP của bạn"
        body = f"Mã OTP của bạn là: {otp_code} \n"
        body += "Mã sẽ có hiệu lực trong vòng 5 phút!"
        
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = config.SENDER_EMAIL
        msg["To"] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config.SMTP_SERVER, config.SMTP_PORT, context=context) as server:
            server.login(config.SENDER_EMAIL, config.APP_PASSWORD)
            server.send_message(msg)
        return True  
    except Exception as e:
        print("Lỗi gửi email:", e)
        return False 
def get_old_passwords(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password, old_password_1, old_password_2 FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user  # Trả về (current_password, old_password_1, old_password_2)
def is_new_password_valid(new_password, old_passwords):
    return new_password not in old_passwords
def is_valid_password(password):
    """Kiểm tra mật khẩu phải trên 8 ký tự và chứa ít nhất 1 ký tự đặc biệt"""
    return len(password) > 8 and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
@users_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")  
    phone = data.get("phone")
    role = data.get("role")
    otp_code = data.get("otp")  

    # Kiểm tra role hợp lệ
    if role not in ["HOTEL_OWNER", "CUSTOMER"]:
        return jsonify({"error": "Role không hợp lệ! Chỉ chấp nhận HOTEL_OWNER hoặc CUSTOMER"}), 400
    if is_valid_password(password):
        return jsonify({"error": "Mật khẩu phải trên 8 kí tự và chứa ít nhất 1 kí tự đặc biệt!"}),400
    # Kiểm tra thông tin đầu vào
    if not username or not email or not password or not phone:
        return jsonify({"error": "Vui lòng nhập đầy đủ username, email, password và phone!"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
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
            cursor.execute("INSERT INTO users (username, email, phone, password, role) VALUES (%s, %s, %s, %s, %s)", 
                           (username, email, phone, password, role))
            conn.commit()
            cursor.close()
            conn.close()
            del otp_storage[email]  # Xóa OTP sau khi xác nhận thành công
            return jsonify({"message": "Đăng ký thành công!"}), 201
        except get_db_connection as err:
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

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Kiểm tra điều kiện: chỉ truyền vào username hoặc email (không cả hai)
    if (username and email) or (not username and not email):
        return jsonify({"error": "Bạn phải nhập username hoặc email, không được nhập cả hai hoặc bỏ trống"}), 400

    identifier = username if username else email  # Chọn giá trị hợp lệ
    field = "username" if username else "email"  # Xác định tìm theo username hay email

    if not password:
        return jsonify({"error": "Password không được để trống"}), 400
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"SELECT username, password FROM users WHERE {field} = %s"
        cursor.execute(query, (identifier,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and user[1] == password:
            access_token = create_access_token(identity=user[0])
            return jsonify({"message": "Đăng nhập thành công", "access_token": access_token}), 200
        else:
            return jsonify({"error": "Sai username/email hoặc password"}), 401

    except get_db_connection.Error as err:
        return jsonify({"error": str(err)}), 500
    
@users_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    email = data.get("email")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
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
    
@users_bp.route("/reset-password", methods=["POST"])
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
    UPDATE users 
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

@users_bp.route("/get_user", methods=["GET"])
def get_user_info():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return {"error": "Unauthorized"}, 401

    token = auth_header.split(" ")[1]  # Lấy token từ "Bearer <token>"
    user = get_user_from_token(token)
    
    if user:
        return {"user_id": user["id"], "role": user["role"]}
    return {"error": "Unauthorized"}, 401