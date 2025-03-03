from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from createdatabase import User, Hotel, Room, Booking, UserRole, Base

# Kết nối cơ sở dữ liệu
DATABASE_URL = "mysql+mysqlconnector://admin:28072003@localhost/hotel_booking_app"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Chèn dữ liệu mẫu
def insert_data():
    # Thêm người dùng
    admin = User(username='admin', password='admin1234', email='luongducmanh02@gmail.com',phone="0925940864", role=UserRole.ADMIN)
    user1 = User(username='user1', password='123456', email='user1@example.com',phone = "0123456789", role=UserRole.HOTEL_OWNER)
    user2 = User(username='user2', password='123456', email='user2@example.com',phone= "02938561234", role=UserRole.CUSTOMER)
    session.add_all([admin, user1, user2])
    session.commit()
    
    # Thêm khách sạn
    hotel1 = Hotel(name='Ha Noi Hotel', location='Ha Noi', owner_id=user1.id)
    session.add(hotel1)
    session.commit()
    
    # Thêm phòng
    room1 = Room(hotel_id=hotel1.id, room_number='101', price=100.0, is_available=True)
    room2 = Room(hotel_id=hotel1.id, room_number='102', price=150.0, is_available=True)
    session.add_all([room1, room2])
    session.commit()
    
    # Thêm đặt phòng
    booking1 = Booking(customer_id=user1.id, room_id=room1.id, check_in=datetime.datetime(2024, 3, 1), check_out=datetime.datetime(2024, 3, 5), status='confirmed')
    session.add(booking1)
    session.commit()
    
    print("Dữ liệu mẫu đã được chèn thành công.")

insert_data()
