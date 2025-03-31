import smtplib
import ssl
from email.message import EmailMessage
from config import Config
import re
from flask_jwt_extended import get_jwt_identity
from db import get_db_connection

def send_email(receiver_email, otp_code):
    try:
        subject = "Mã OTP của bạn"
        body = f"Mã OTP của bạn là: {otp_code} \n"
        body += "Mã sẽ có hiệu lực trong vòng 5 phút!"
        
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = Config.SENDER_EMAIL
        msg["To"] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(Config.SMTP_SERVER, Config.SMTP_PORT, context=context) as server:
            server.login(Config.SENDER_EMAIL, Config.APP_PASSWORD)
            server.send_message(msg)
        return True  
    except Exception as e:
        print("Lỗi gửi email:", e)
        return False 
def get_old_passwords(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password, old_password_1, old_password_2 FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user  
def is_new_password_valid(new_password, old_passwords):
    return new_password not in old_passwords
def is_valid_password(password):
    """Kiểm tra mật khẩu phải trên 8 ký tự và chứa ít nhất 1 ký tự đặc biệt"""
    return len(password) > 8 and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
def get_username_from_token():
    """Lấy username từ JWT token của người dùng đã đăng nhập."""
    username = get_jwt_identity()  # Lấy giá trị identity từ token
    return username