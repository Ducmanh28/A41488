from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection

hotels_bp = Blueprint("hotels", __name__)
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
def get_hotel(hotel_id):
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