from flask import Blueprint, request, jsonify
from db import get_db_connection

hotels_bp = Blueprint("hotels", __name__)
@hotels_bp.route("/hotels/<int:hotel_id>", methods=["GET"])
def get_hotel(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM hotels WHERE id = %s",(hotel_id, ))
    hotels = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(hotels)
@hotels_bp.route("/hotels", methods=["GET"])
def get_all_hotels():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM hotels")
    hotels = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(hotels)
@hotels_bp.route("/hotels/find", methods=["POST"])
def find_hotel():
    data = request.json
    area = data.get("area")
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    status = "Available"
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Lấy danh sách khách sạn theo khu vực
    cursor.execute("SELECT * FROM hotels WHERE area = %s AND status = %s",(area,status ))
    hotels = cursor.fetchall()

    # Kiểm tra nếu bảng busy_room không có dữ liệu
    cursor.execute("SELECT COUNT(*) as total FROM busy_room")
    total_busy_rooms = cursor.fetchone()["total"]

    if total_busy_rooms == 0:
        cursor.close()
        conn.close()
        return jsonify(hotels)  

    # Danh sách khách sạn có phòng trống
    available_hotels = []

    for hotel in hotels:
        hotel_id = hotel["id"]
        
        # Kiểm tra số lượng phòng bị bận trong khoảng thời gian nhập vào
        cursor.execute("""
            SELECT COUNT(*) as busy_count FROM busy_room 
            WHERE hotel_id = %s AND (
                (busy_from <= %s AND busy_to > %s) OR
                (busy_from < %s AND busy_to >= %s) OR
                (busy_from >= %s AND busy_to <= %s)
            )
        """, (hotel_id, check_in, check_in, check_out, check_out, check_in, check_out))

        busy_count = cursor.fetchone()["busy_count"] or 0

        # Nếu không có phòng nào bị bận, thêm khách sạn vào danh sách khả dụng
        if busy_count == 0:
            available_hotels.append(hotel)

    cursor.close()
    conn.close()
    return jsonify(available_hotels)
@hotels_bp.route("/hotels/<int:hotel_id>/roomtypes",methods=["GET"])
def get_roomtypes_of_hotels(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * from roomtypes WHERE hotel_id = %s",(hotel_id, ))
    hotels = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(hotels)
@hotels_bp.route("/roomtypes/<int:roomtypes_id>",methods=["GET"])
def get_room_info(roomtypes_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM roomtypes WHERE id = %s",(roomtypes_id, ))
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(data)
@hotels_bp.route("/additionalservices",methods=["GET"])
def get_addtional_services():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM additionalservices")
    data = cursor.fetchall()
    return jsonify(data)
