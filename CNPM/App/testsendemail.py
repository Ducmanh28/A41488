import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_otp():
    return str(random.randint(100000, 999999))  # Tạo OTP 6 chữ số

def send_email_otp(receiver_email, otp):
    sender_email = "luongducmanh02@gmail.com@gmail.com"
    sender_password = "Ducmanh2873."  # Sử dụng App Password thay vì mật khẩu thật
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Mã OTP của bạn"
    
    body = f"Mã OTP của bạn là: {otp}. Mã này có hiệu lực trong 5 phút."
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Lỗi gửi email:", e)
        return False

# Ví dụ sử dụng
otp = generate_otp()
send_email_otp("ditmemayconlon1234@gmail.com", otp)
