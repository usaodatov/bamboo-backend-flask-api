# app.py
# Bamboo Backend Flask API
# Author: Umid Saodatov
# Date: 2025
# Description: Handles ping and message endpoints for an e-commerce demo backend.

from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for the frontend at umexim.com
CORS(app, origins=["https://umexim.com"])

# Add CORS headers to every response
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "https://umexim.com")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    return response

# Simple health check endpoint
@app.route("/api/ping", methods=["GET", "OPTIONS"])
def ping():
    if request.method == "OPTIONS":
        return '', 204  # CORS preflight
    return jsonify({"message": "Bamboo Backend Server is OPERATIONAL and here is PONG from backend"})

# Handle message sent from the frontend
@app.route("/api/message", methods=["POST", "OPTIONS"])
def message():
    if request.method == "OPTIONS":
        return '', 204  # CORS preflight
    data = request.get_json()
    user_message = data.get("text", "")
    reply = f"Bamboo Backend Server is OPERATIONAL and has RECEIVED the following message: {user_message}"
    return jsonify({"response": reply})

# Run locally only (not used in production with Gunicorn)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

