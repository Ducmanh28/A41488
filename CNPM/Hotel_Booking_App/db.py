import mysql.connector
from config import Config

def get_db_connection():
    return mysql.connector.connect(**Config.DB_CONFIG)

import mysql.connector

def update_hotel_image(hotel_name):
    # Tạo phiên bản tên thường không dấu và thay khoảng trắng bằng gạch dưới (nếu cần)
    hotel_name_lower = hotel_name.lower().replace(" ", "_")

    # Tạo URL ảnh theo yêu cầu
    image_url = f"/CNPM/Hotel_Booking_App/font/Hotel/{hotel_name}/{hotel_name_lower}.jpg"

    # Kết nối MySQL
    conn = get_db_connection()
    cursor = conn.cursor()

    # Cập nhật image_url trong bảng hotels
    query = "UPDATE hotels SET image_url = %s WHERE hotel_name = %s"
    cursor.execute(query, (image_url, hotel_name))

    # Commit và đóng kết nối
    conn.commit()
    cursor.close()
    conn.close()

    print(f"Đã cập nhật ảnh cho khách sạn '{hotel_name}': {image_url}")

update_hotel_image("Grand_Hotel")
update_hotel_image("Cozy_Homestay")
update_hotel_image("Eco_Lodge")
update_hotel_image("Lakeview_Inn")
update_hotel_image("Mountain_Retreat")
update_hotel_image("Ocean_View")
update_hotel_image("Paradise_Resort")
update_hotel_image("Royal_Palace")
update_hotel_image("Skyline_Hotel")
update_hotel_image("Sunshine_Hotel")