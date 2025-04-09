from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection

payment_bp = Blueprint("payment",__name__)

@payment_bp.route("/payment/vnpay",methods=["POST"])
@jwt_required()
def payment_vnpay():
    data = request.json
    invoices_id = data.get("invoices_id")
    state = "DA THANH TOAN"
    type_of_payment = "VNPAY"
    pay_money = float(data.get("total_money"))
    pay_description = data.get("description")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT total_price FROM invoices WHERE id = %s",(invoices_id, ))
    total = cursor.fetchone()
    if total:
        total_price = total.get("total_price")
    else:
        return jsonify({"message": "Lỗi lấy dữ liệu giá"})
    if total_price == 0.7*pay_money:
        cursor.execute("INSERT INTO payment (invoices_id,total_money,pay_description,type_of_payment) VALUES  (%s,%s,%s,%s)",(invoices_id,pay_money,pay_description,type_of_payment))
        conn.commit()
        cursor.execute("UPDATE invoices SET state =%s WHERE id = %s",(state,invoices_id))
        conn.commit()
        return jsonify({"message": f"Thanh Toán thành công đơn hàng {invoices_id} bằng VNPAY!"}),201
    else:
        return jsonify({"message": "Vui lòng thanh toán đúng số tiền!"})
    
@payment_bp.route("/payment/card",methods=["POST"])
@jwt_required()
def payment_card():
    data = request.json
    invoices_id = data.get("invoices_id")
    state = "DA THANH TOAN"
    type_of_payment = "card"
    card_number = data.get("card_number")
    card_type = data.get("card_type")
    pay_money = float(data.get("total_money"))
    print(0.7*pay_money)
    pay_description = data.get("description")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT total_price FROM invoices WHERE id = %s",(invoices_id, ))
    total = cursor.fetchone()
    if total:
        total_price = total.get("total_price")
        print(total_price)
    else:
        return jsonify({"message": "Lỗi lấy dữ liệu giá"})
    if total_price*0.7 == pay_money:
        cursor.execute("INSERT INTO payment (invoices_id,total_money,pay_description,type_of_payment,card_number,card_type) VALUES  (%s,%s,%s,%s,%s,%s)",(invoices_id,pay_money,pay_description,type_of_payment,card_number,card_type))
        conn.commit()
        cursor.execute("UPDATE invoices SET state =%s WHERE id = %s",(state,invoices_id))
        conn.commit()
        return jsonify({"message": f"Thanh Toán thành công đơn hàng {invoices_id} bằng {card_type}!"}),201
    else:
        return jsonify({"message": "Vui lòng thanh toán đúng số tiền!"})