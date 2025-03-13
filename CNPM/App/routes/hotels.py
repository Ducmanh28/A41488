from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection

hotels_bp = Blueprint("hotels", __name__)
@hotels_bp.route("/hotels", methods=["GET"])
@jwt_required()
def get_info_hotel_owner(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s",(username, ))
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)
@hotels_bp.route("/hotels", methods=["POST"])
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
@hotels_bp.route("/hotels/<int:hotel_id>", methods=["GET"])
def get_hotels(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM hotels WHERE id = %s",(hotel_id, ))
    hotels = cursor.fetchall()
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
@hotels_bp.route("/hotels/<int:hotel_id>", methods=["PUT"])
@jwt_required()
def update_hotel(hotel_id):
    data = request.json
    name = data.get("name")
    location = data.get("location")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE hotels SET location = %s, name = %s WHERE id = %s", (location, name, hotel_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Hotel updated successfully"}), 201
@hotels_bp.route("/hotels/<int:hotel_id>", methods=["DELETE"])
@jwt_required()
def deleted_hotel(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hotels WHERE id = %s", (hotel_id, ))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Hotel deleted successfully"}), 201
@hotels_bp.route("/hotels/<int:hotel_id>/rooms", methods=["POST"])
@jwt_required()
def create_room(hotel_id):
    data = request.json
    room_number = data.get("room_number")
    room_type = data.get("room_type")
    price = data.get("price")
    description = data.get("description")
    is_available = 1
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rooms (hotel_id,room_number,room_type,price,is_available,description) VALUES (%s, %s, %s, %s, %s, %s)", (hotel_id,room_number,room_type,price,is_available,description ))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Room added successfully"}), 201
@hotels_bp.route("/hotels/<int:hotel_id>/rooms/<int:rooms_id>", methods=["PUT"])
@jwt_required()
def update_room(hotel_id,rooms_id):
    data = request.json
    room_number = data.get("room_number")
    room_type = data.get("room_type")
    price = data.get("price")
    description = data.get("description")
    is_available = 1
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE rooms SET room_number = %s,room_type = %s,price =%s, is_available = %s,description= %s WHERE id = %s and hotel_id = %s", (room_number,room_type,price,is_available,description,rooms_id,hotel_id ))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Room updated successfully"}), 201
@hotels_bp.route("/hotels/<int:hotel_id>/rooms/<int:room_id>", methods=["DELETE"])
@jwt_required()
def deleted_rooms(hotel_id,room_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hotels WHERE id = %s and hotel_id = %s", (room_id, hotel_id ))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Room deleted successfully"}), 201
@hotels_bp.route("/hotels/<int:hotel_id>/rooms/<int:room_id>", methods=["GET"])
def get_rooms(room_id, hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rooms WHERE id = %s AND hotel_id = %s", (room_id, hotel_id))
    rooms = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(rooms)
@hotels_bp.route("/hotels/<int:hotel_id>/rooms", methods=["GET"])
def get_all_rooms(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rooms WHERE hotel_id = %s",(hotel_id, ))
    rooms = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(rooms)
