from flask import Blueprint, request, jsonify
from services.ai_service import generate_reply
from services.email_service import send_email
from services.storage_service import store_query

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["POST"])
def contact():

    data = request.json
    email = data["email"]
    message = data["message"]

    ai_reply = generate_reply(message)

    send_email(
        email,
        "Support Team Response",
        ai_reply
    )

    store_query(email, message, ai_reply)

    return jsonify({
        "status": "success",
        "reply": ai_reply
    })