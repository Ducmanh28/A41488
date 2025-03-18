from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection

bookings_bp = Blueprint("bookings", __name__)

@bookings_bp.route("/bookings", methods=["POST"])
@jwt_required()
def create_booking():
    data = request.json
    user_id = data.get("user_id")
    room_id = data.get("room_type_id")
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    total_price = data.get("total_price")
    
    if not all([user_id, room_id, check_in, check_out]):
        return jsonify({"error": "Thiếu thông tin đặt phòng"}), 400
    if check_in >= check_out:
        return jsonify({"error": "Ngày check-in phải trước ngày check-out"}), 400
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Thêm booking mới
        cursor.execute("INSERT INTO bookings (user_id, room_type_id, check_in, check_out, total_price) VALUES (%s, %s, %s, %s)", 
                       (user_id, room_id, check_in, check_out,total_price))
        
        conn.commit()
        return jsonify({"message": "Đặt phòng thành công"}), 201

    except get_db_connection.Error as err:
        conn.rollback()
        return jsonify({"error": str(err)}), 500

    finally:
        cursor.close()
        conn.close()
@bookings_bp.route("/bookings", methods=["GET"])
@jwt_required()
def get_bookings():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bookings")
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(bookings)
@bookings_bp.route("/bookings/<int:booking_id>",methods=["DELETE"])
@jwt_required()
def delete_booking(booking_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE * FROM bookings WHERE id = %s",(booking_id, ))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Booking deleted successfully"}), 201