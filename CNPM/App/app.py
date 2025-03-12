from flask import Flask, request, jsonify
import mysql.connector
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
import random
import datetime
import random
from time import time
otp_storage = {}
app = Flask(__name__)
jwt = JWTManager(app)
# Cấu hình JWT
app.config["JWT_SECRET_KEY"] = "thanglonguni1234"
# Cấu hình MySQL
db_config = {
    "host": "localhost",
    "user": "admin",
    "password": "28072003",
    "database": "hotel_booking_app"
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
    password = data.get("password")
    phone = data.get("phone")
    role = data.get("role")
    if role == "HOTEL_OWNER" or role == "CUSTOMER":
        if not username or not email or not password or not phone:
            return jsonify({"error": "Username, email, password hoặc role không được để trống"}), 400
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email,phone, password,role) VALUES (%s, %s, %s, %s, %s)", 
                        (username, email,phone, password,role))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Đăng ký thành công"}), 201
        except mysql.connector.Error as err:
            return jsonify({"error": str(err)}), 500
    else:
        return jsonify({"message": "Vui lòng kiểm tra lại role: HOTEL_OWNER hoặc CUSTOMER!"}), 400
# Đăng nhập bằng username hoặc email
@app.route("/login", methods=["POST"])
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

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json
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
@app.route("/hotels", methods=["POST"])
@jwt_required()
def create_hotel():
    data = request.json
    name = data.get("name")
    location = data.get("location")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hotels (name, location) VALUES (%s, %s)", (name, location))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Hotel added successfully"}), 201

@app.route("/hotels", methods=["GET"])
def get_hotels():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM hotels")
    hotels = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(hotels)

@app.route("/hotels/<int:hotel_id>", methods=["PUT"])
@jwt_required()
def update_hotel(hotel_id):
    data = request.json
    name = data.get("name")
    location = data.get("location")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE hotels SET name = %s, location = %s WHERE id = %s", (name, location, hotel_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Hotel updated successfully"})

@app.route("/hotels/<int:hotel_id>", methods=["DELETE"])
@jwt_required()
def delete_hotel(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hotels WHERE id = %s", (hotel_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Hotel deleted successfully"})

# 🏠 CRUD Room
@app.route("/rooms", methods=["POST"])
@jwt_required()
def create_room():
    data = request.json
    hotel_id = data.get("hotel_id")
    room_type = data.get("room_type")
    price = data.get("price")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rooms (hotel_id, room_type, price) VALUES (%s, %s, %s)", (hotel_id, room_type, price))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Room added successfully"}), 201

@app.route("/rooms", methods=["GET"])
def get_rooms():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(rooms)

# 📅 CRUD Booking
@app.route("/bookings", methods=["POST"])
@jwt_required()
def create_booking():
    data = request.json
    user_id = data.get("user_id")
    room_id = data.get("room_id")
    check_in = data.get("check_in")
    check_out = data.get("check_out")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (user_id, room_id, check_in, check_out) VALUES (%s, %s, %s, %s)", (user_id, room_id, check_in, check_out))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Booking created successfully"}), 201

@app.route("/bookings", methods=["GET"])
@jwt_required()
def get_bookings():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bookings")
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(bookings)

# API bảo vệ bằng token
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"message": "Bạn đã truy cập vào API bảo vệ bằng token!"}), 200


if __name__ == "__main__":
    app.run(debug=True)
