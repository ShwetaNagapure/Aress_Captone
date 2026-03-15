from flask import Blueprint, request, jsonify
from services.openai_service import generate_reply
from services.email_service import send_email

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/api/contact", methods=["POST"])
def contact():

    data = request.json

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    reply = generate_reply(message)

    email_body = f"""
    Dear {name},

    Thank you for contacting our support team.

    Your Query:
    {message}

    Our Response:
    {reply}

    Best Regards,
    AI Support Team
    """

    send_email(email, "Support Response", email_body)

    return jsonify({
        "status": "success",
        "ai_response": reply
    })