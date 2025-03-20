from db import get_db_connection
import hashlib
import hmac
import requests
from flask import Blueprint, request, jsonify
payments_bp = Blueprint("customers", __name__)

MOMO_PARTNER_CODE = "MOMOXXXXXX"
MOMO_ACCESS_KEY = "XXXXXXXXXXXXXXXX"
MOMO_SECRET_KEY = "XXXXXXXXXXXXXXXX"
MOMO_API_URL = "http://test-payment.momo.vn/v2/gateway/api/create"

MOMO_IPN_URL = "http://127.0.0.1:5000/payment/momo/callback"
MOMO_REDIRECT_URL = "http://127.0.0.1:5000/payment/success"


@payments_bp.route("/payment/momo/create", methods=["POST"])
def create_momo_payment():
    data = request.json
    order_id = f"ORDER{data['booking_id']}"
    amount = data["amount"]
    request_id = f"REQ{data['booking_id']}"
    order_info = "Thanh toán đặt phòng khách sạn"

    # Chuỗi raw data cần ký
    raw_data = f"accessKey={MOMO_ACCESS_KEY}&amount={amount}&extraData=&ipnUrl={MOMO_IPN_URL}" \
               f"&orderId={order_id}&orderInfo={order_info}&partnerCode={MOMO_PARTNER_CODE}" \
               f"&redirectUrl={MOMO_REDIRECT_URL}&requestId={request_id}&requestType=captureWallet"

    # Tạo chữ ký HMAC SHA256
    signature = hmac.new(
        MOMO_SECRET_KEY.encode('utf-8'),
        raw_data.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    # Dữ liệu gửi đến MoMo
    payload = {
        "partnerCode": MOMO_PARTNER_CODE,
        "accessKey": MOMO_ACCESS_KEY,
        "requestId": request_id,
        "amount": amount,
        "orderId": order_id,
        "orderInfo": order_info,
        "redirectUrl": MOMO_REDIRECT_URL,
        "ipnUrl": MOMO_IPN_URL,
        "extraData": "",
        "requestType": "captureWallet",
        "signature": signature,
        "lang": "vi"
    }

    # Gửi request đến MoMo
    response = requests.post(MOMO_API_URL, json=payload)
    response_data = response.json()

    return jsonify(response_data)

# Xử lý callback từ MoMo
@app.route("/payment/momo/callback", methods=["POST"])
def momo_callback():
    data = request.json

    # Chuỗi raw data cần ký để kiểm tra chữ ký
    raw_data = f"accessKey={MOMO_ACCESS_KEY}&amount={data['amount']}&extraData={data['extraData']}" \
               f"&message={data['message']}&orderId={data['orderId']}&orderInfo={data['orderInfo']}" \
               f"&partnerCode={data['partnerCode']}&requestId={data['requestId']}" \
               f"&responseTime={data['responseTime']}&resultCode={data['resultCode']}&transId={data['transId']}"

    signature_check = hmac.new(
        MOMO_SECRET_KEY.encode('utf-8'),
        raw_data.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    if signature_check != data["signature"]:
        return jsonify({"status": "error", "message": "Invalid signature"}), 400

    # Kiểm tra kết quả giao dịch
    if data["resultCode"] == 0:
        return jsonify({"status": "success", "message": "Thanh toán thành công"})
    else:
        return jsonify({"status": "failed", "message": "Thanh toán thất bại"})