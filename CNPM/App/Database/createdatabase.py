import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, DateTime, Float, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import enum
import datetime

Base = declarative_base()

# Enum cho vai trò người dùng
class UserRole(enum.Enum):
    CUSTOMER = "customer"
    HOTEL_OWNER = "hotel_owner"
    ADMIN = "admin"

# Bảng User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    hotels = relationship("Hotel", back_populates="owner")
    bookings = relationship("Booking", back_populates="customer")

# Bảng Khách sạn
class Hotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="hotels")
    rooms = relationship("Room", back_populates="hotel")

# Bảng Phòng
class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    room_number = Column(String(5), nullable=False)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)
    hotel = relationship("Hotel", back_populates="rooms")
    bookings = relationship("Booking", back_populates="room")

# Bảng Đặt phòng
class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('users.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    status = Column(String(50), default="pending")
    customer = relationship("User", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")

# Tạo database nếu chưa tồn tại
def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='admin',
            password='28072003'
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_booking_app")
        print("Database 'hotel_booking_app' đã được tạo hoặc đã tồn tại.")
    except Error as e:
        print(f"Lỗi tạo database: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

create_database()

# Kết nối cơ sở dữ liệu MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='admin',
    password='28072003',
    database='hotel_booking_app'
)

if connection.is_connected():
    print("Kết nối MySQL thành công")

# Tạo engine SQLAlchemy
DATABASE_URL = "mysql+mysqlconnector://admin:28072003@localhost/hotel_booking_app"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Tạo bảng
Base.metadata.create_all(engine)