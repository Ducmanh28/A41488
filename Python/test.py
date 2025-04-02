import mysql.connector

# Thiết lập thông tin kết nối
config = {
    'user': 'admin',         # Thay 'root' bằng username của bạn
    'password': '28072003', # Thay 'yourpass' bằng mật khẩu của bạn
    'host': 'localhost',    # Nếu MySQL chạy trên máy cục bộ
    'database': 'hotel_booking_app'    # Tên database bạn muốn kết nối
}

try:
    # Tạo kết nối
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print("Kết nối thành công đến MySQL Server!")
    
    # Tạo cursor để thực hiện truy vấn
    cursor = conn.cursor()
    
    # Kiểm tra danh sách bảng trong database
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)

except mysql.connector.Error as e:
    print(f"Lỗi kết nối: {e}")

finally:
    # Đóng kết nối khi không sử dụng nữa
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Đã đóng kết nối.")
