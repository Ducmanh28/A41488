from flask import Flask
from flask_jwt_extended import JWTManager
from config import JWT_SECRET_KEY
from routes.users import users_bp
from routes.hotels import hotels_bp
#from routes.rooms import rooms_bp
#from routes.bookings import bookings_bp

app = Flask(__name__)

# Cấu hình JWT
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
jwt = JWTManager(app)

# Đăng ký route
app.register_blueprint(users_bp)
app.register_blueprint(hotels_bp)
#app.register_blueprint(rooms_bp)
#app.register_blueprint(bookings_bp)

if __name__ == "__main__":
    app.run(debug=True)
