from flask import Flask, jsonify, request, send_file
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from routes.auth import auth_bp
from routes.csv_processor import csv_bp
from routes.contact import contact_bp
from routes.projects import projects_bp
from database import init_db
from datetime import timedelta

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": [
    "http://localhost:5173",  # Local development
    "https://www.nico-rodriguez.com",  # Your domain
    "https://n1ckrod-website-frontend.vercel.app"  # Your Vercel domain
]}})

# Configuration
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key')  # Change in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESUME_PATH'] = 'static/resume.pdf'

jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(csv_bp, url_prefix='/api')
app.register_blueprint(contact_bp, url_prefix='/api')
app.register_blueprint(projects_bp, url_prefix='/api')

# Ensure required directories exist
for directory in ['uploads', 'static']:
    if not os.path.exists(directory):
        os.makedirs(directory)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"message": "Server is running"}), 200

@app.route('/api/resume', methods=['GET'])
def get_resume():
    try:
        return send_file(app.config['RESUME_PATH'], as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "Resume not found"}), 404

# Initialize database
init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)