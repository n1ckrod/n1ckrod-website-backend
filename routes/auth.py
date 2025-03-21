from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing fields'}), 400

    hashed_password = generate_password_hash(password)

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
            conn.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    with get_db_connection() as conn:
        c = conn.cursor()
        user = c.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

    if user and check_password_hash(user[2], password):
        access_token = create_access_token(identity=email)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
