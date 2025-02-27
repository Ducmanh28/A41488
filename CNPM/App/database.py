
import mysql.connector

# Thông tin kết nối MySQL
MYSQL_HOST = "localhost"
MYSQL_USER = "admin"  # Thay bằng user của bạn
MYSQL_PASSWORD = "28072003"  # Thay bằng mật khẩu của bạn
DATABASE_NAME = "hotel_db"

# Kết nối tới MySQL
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)
cursor = conn.cursor()

# Tạo database nếu chưa có
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};")
print(f"Database '{DATABASE_NAME}' đã được tạo hoặc đã tồn tại.")

# Chọn database
conn.database = DATABASE_NAME

# Tạo bảng users nếu chưa có
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
"""
cursor.execute(create_table_query)
print("Bảng 'users' đã được tạo hoặc đã tồn tại.")

# Chèn dữ liệu mẫu
insert_query = """
INSERT INTO users (username, email, password)
VALUES (%s, %s, %s)
"""
users_data = [
    #("admin", "admin@example.com", "admin123"),
    #("user1", "user1@example.com", "password1"),
    #("user2", "user2@example.com", "password2"),
]

# Thêm dữ liệu vào bảng, bỏ qua nếu username hoặc email đã tồn tại
for user in users_data:
    try:
        cursor.execute(insert_query, user)
        conn.commit()
        print(f"Thêm user {user[0]} thành công.")
    except mysql.connector.Error as err:
        print(f"Lỗi khi thêm user {user[0]}: {err}")

# Đóng kết nối
cursor.close()
conn.close()
print("Hoàn thành.")
