from flask import Blueprint, request, jsonify
import pandas as pd
import os

csv_bp = Blueprint('csv_processor', __name__)

@csv_bp.route('/process-csv', methods=['POST'])
def process_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and file.filename.endswith('.csv'):
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        # Process CSV
        df = pd.read_csv(filepath)
        summary = df.describe().to_json()  # Convert to JSON

        os.remove(filepath)  # Clean up

        return jsonify({'message': 'File processed successfully', 'summary': summary}), 200
    return jsonify({'error': 'Invalid file type'}), 400
