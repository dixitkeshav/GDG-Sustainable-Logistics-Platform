from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint("auth", __name__)

users = {"admin": generate_password_hash("password")}
@auth_bp.route("/login", methods=["POST"])
def login():
    print("Received Headers:", request.headers)  # Debugging
    print("Received Data:", request.data)  # Debugging

    if request.method != "POST":
        return jsonify({"error": "Method not allowed"}), 405 

    if request.content_type != "application/json":
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username], password):
        return jsonify({"message": "Login successful", "token": "fake-jwt-token"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
