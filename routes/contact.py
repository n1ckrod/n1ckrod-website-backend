from flask import Blueprint, request, jsonify
import smtplib
from email.mime.text import MIMEText
import os

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['POST'])
def send_contact_email():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not all([name, email, message]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Configure your email settings here
        smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('SMTP_PORT', 587))
        smtp_username = os.getenv('SMTP_USERNAME')
        smtp_password = os.getenv('SMTP_PASSWORD')
        recipient_email = os.getenv('RECIPIENT_EMAIL')

        msg = MIMEText(f"From: {name}\nEmail: {email}\n\n{message}")
        msg['Subject'] = f"Portfolio Contact Form: Message from {name}"
        msg['From'] = smtp_username
        msg['To'] = recipient_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 