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
@admin_bp.route("/admin/hotels/create",methods=["POST"])
@jwt_required()
def create_hotels():
    data = request.json
    name = data.get("name")
    address = data.get("address")
    area = data.get("area")
    hotline = data.get("hotline")
    rate = data.get("rate")
    image_url = data.get("image_url")
    description = data.get("description")
    status = data.get("status")
    review_score = data.get("review_score")
    price = data.get("price")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hotels(name,address,area,hotline,rate,image_url,description,status,review_score,price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                   ,(name,address,area,hotline,rate,image_url,description,status,review_score,price))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Đã tạo thành công!"})
@admin_bp.route("/admin/hotels/<int:hotel_id>",methods=["PUT"])
@jwt_required()
def update_hotel(hotel_id):
    data = request.json
    if not data:
        return jsonify({"error": "Dữ liệu cập nhật không hợp lệ"}), 400

    fields = []
    values = []
    if "name" in data:
        fields.append("name = %s")
        values.append(data["name"])
    if "hotline" in data:
        fields.append("hotline = %s")
        values.append(data["hotline"])
    if "address" in data:
        fields.append("address = %s")
        values.append(data["address"])
    if "price" in data:
        fields.append("price = %s")
        values.append(data["price"])
    if "area" in data:
        fields.append("area = %s")
        values.append(data["area"])
    if "description" in data:
        fields.append("description = %s")
        values.append(data["description"])
    if "rate" in data:
        fields.append("rate = %s")
        values.append(data["rate"])
    if "review_score" in data:
        fields.append("review_score = %s")
        values.append(data["review_score"])
    if "image_url" in data:
        fields.append("image_url = %s")
        values.append(data["image_url"])
    if "status" in data:
        fields.append("status = %s")
        values.append(data["status"])
    if not fields:
        return jsonify({"error": "Không có thông tin nào để cập nhật"}), 400

    # Ghép câu lệnh SQL
    query = f"UPDATE hotels SET {', '.join(fields)} WHERE id = %s"
    values.append(hotel_id)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Hotel updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@admin_bp.route("/admin/hotels/<int:hotel_id>",methods=["DELETE"])
@jwt_required()
def delete_hotel(hotel_id):
    conn = get_db_connection()
    conn.cursor().execute("DELETE FROM roomtypes WHERE hotel_id = %s",(hotel_id, ))
    conn.commit()
    conn.cursor().execute("DELETE FROM hotels WHERE id = %s",(hotel_id, ))
    conn.commit()
    conn.cursor().close()
    conn.close()
    return jsonify({"message": f"Delete complete hotel {hotel_id}"})
@admin_bp.route("/admin/hotels/<int:hotel_id>/roomtypes",method=["GET"])
@jwt_required()
def get_room_of_hotel(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM roomtypes WHERE hotel_id = %s",(hotel_id, ))
    rooms = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rooms)
@admin_bp.route("/admin/roomtypes",methods=["GET"])
@jwt_required()
def get_all_roomtype():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM roomtypes")
    rooms = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rooms)
@admin_bp.route("/admin/roomtypes/<int:roomtype_id>",methods=["PUT"])
@jwt_required()
def update_room(roomtype_id):
    data = request.json
    if not data:
        return jsonify({"error": "Dữ liệu cập nhật không hợp lệ"}), 400

    fields = []
    values = []
    if "name" in data:
        fields.append("name = %s")
        values.append(data["name"])
    if " capacity" in data:
        fields.append("capacity = %s")
        values.append(data["capacity"])
    if "bed_type" in data:
        fields.append("bed_type = %s")
        values.append(data["bed_type"])
    if "price" in data:
        fields.append("price = %s")
        values.append(data["price"])
    if "rating" in data:
        fields.append("rating = %s")
        values.append(data["rating"])
    if "availability" in data:
        fields.append("availability = %s")
        values.append(data["availability"])
    if "services" in data:
        fields.append("services = %s")
        values.append(data["services"])
    if "area" in data:
        fields.append("area = %s")
        values.append(data["area"])
    if "img_url" in data:
        fields.append("img_url = %s")
        values.append(data["img_url"])
    if "hotel_id" in data:
        fields.append("hotel_id = %s")
        values.append(data["hotel_id"])
    if not fields:
        return jsonify({"error": "Không có thông tin nào để cập nhật"}), 400

    # Ghép câu lệnh SQL
    query = f"UPDATE roomtypes SET {', '.join(fields)} WHERE id = %s"
    values.append(roomtype_id)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Roomtype updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@admin_bp.route("/admin/roomtypes/create",methods=["POST"])
@jwt_required()
def create_rooms():
    data = request.json
    name = data.get("name")
    hotel_id = data.get("hotel_id")
    area = data.get("area")
    services = data.get("services")
    capacity = data.get("capacity")
    image_url = data.get("image_url")
    bed_type = data.get("bed_type")
    rating = data.get("rating")
    availability = data.get("review_score")
    price = data.get("price")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO roomtypes(name,capacity,area,hotel_id,rating,img_url,bed_type,availability,price,services) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                   ,(name,capacity,area,hotel_id,rating,image_url,bed_type,availability,price,services))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Đã tạo thành công!"})
@admin_bp.route("/admin/roomtypes/<int:roomtype_id>",methods=["DELETE"])
@jwt_required()
def delete_room(roomtype_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM roomtypes WHERE id = %s",(roomtype_id, ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Đã xóa thành công"})
@admin_bp.route("/admin/additionalservices",method=["POST"])
@jwt_required()
def create_additionalservices():
    data = request.json
    name = data.get("service_name")
    price = data.get("price")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO additionalservices(service_name,price) VALUES(%s,%s)",(name,price))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Thêm dịch vụ thành công"})

