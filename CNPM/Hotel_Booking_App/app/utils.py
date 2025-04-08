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
    cursor.execute("SELECT password, old_password_1, old_password_2 FROM customers WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user  
def is_new_password_valid(new_password, old_passwords):
    return new_password not in old_passwords
def is_valid_password(password):
    """Kiểm tra mật khẩu phải trên 8 ký tự và chứa ít nhất 1 ký tự đặc biệt"""
    return len(password) > 8 and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
def get_userid_from_token():
    user_name = get_jwt_identity()
    conn = get_db_connection()
    curosr = conn.cursor()
    curosr.execute("SELECT id FROM customers WHERE username = %s",(user_name, ))
    user_id = curosr.fetchone()
    curosr.close()
    conn.close()
    if user_id:
        return user_id[0]
    return None
def get_hotel_id_from_room_id(room_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT hotel_id FROM roomtypes WHERE id = %s", (room_id, ))
    hotel_id_tuple = cursor.fetchone()
    cursor.close()
    conn.close()
    if hotel_id_tuple:
        return hotel_id_tuple[0]
    return None
