from flask import Blueprint, jsonify
import json
import os

projects_bp = Blueprint('projects', __name__)

def load_projects():
    try:
        with open('data/projects.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@projects_bp.route('/projects', methods=['GET'])
def get_projects():
    projects = load_projects()
    return jsonify(projects), 200 