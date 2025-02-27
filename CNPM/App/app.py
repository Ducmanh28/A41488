from flask import Flask, request, jsonify
import mysql.connector
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
import random
import datetime
import smtplib
from time import time
otp_storage = {}
app = Flask(__name__)
# Cấu hình JWT
app.config["JWT_SECRET_KEY"] = "thanglonguni1234"
bcrypt = Bcrypt(app)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["5 per minute"])
jwt = JWTManager(app)
# Cấu hình MySQL
db_config = {
    "host": "localhost",
    "user": "admin",
    "password": "28072003",
    "database": "hotel_db"
}
# Kết nối database
def get_db_connection():
    return mysql.connector.connect(**db_config)
# Đăng ký tài khoản
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = bcrypt.generate_password_hash(data['password']).decode('utf-8')  

    if not username or not email or not password:
        return jsonify({"error": "Username, email và password không được để trống"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                       (username, email, password))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Đăng ký thành công"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
# Đăng nhập bằng username hoặc email
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    identifier = data['identifier']  # Có thể là username hoặc email
    password = data['password']
    cursor = mysql.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s OR email=%s", (identifier, identifier))
    user = cursor.fetchone()
    cursor.close()
    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=user['id'], expires_delta=datetime.timedelta(hours=1))
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    email = data.get("email")

    # Tạo cursor từ db (thay vì mysql.connection)
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

    return jsonify({"message": "Email hợp lệ", "otp": otp_code})
@app.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.json
    email = data.get("email")
    otp_code = data.get("otp")
    new_password = data.get("new_password")

    if not email or not otp_code or not new_password:
        return jsonify({"error": "Email, OTP và mật khẩu mới không được để trống"}), 400

    # Kiểm tra OTP
    if email not in otp_storage or otp_storage[email]["otp"] != otp_code:
        return jsonify({"error": "Mã OTP không hợp lệ hoặc đã hết hạn"}), 400

    # Cập nhật mật khẩu
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_password, email))
    conn.commit()
    cursor.close()
    conn.close()

    # Xóa OTP sau khi sử dụng
    del otp_storage[email]

    return jsonify({"message": "Đặt lại mật khẩu thành công"}), 200
# API bảo vệ bằng token
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"message": "Bạn đã truy cập vào API bảo vệ bằng token!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
