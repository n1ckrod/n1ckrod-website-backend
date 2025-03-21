from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from routes.auth import auth_bp
from routes.csv_processor import csv_bp
from database import init_db
from datetime import timedelta


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Secure JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Tokens expire after 1 hour
jwt = JWTManager(app)

# Register Blueprints (Modular Routes)
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(csv_bp, url_prefix='/api')

# Ensure uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Initialize database on startup
init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)