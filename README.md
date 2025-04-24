# Bamboo Backend Flask API

This repository contains the backend application built using Python Flask. It provides two RESTful API endpoints (`/api/ping` and `/api/message`) for testing frontend-backend communication in an e-commerce client-server model.

This backend is deployed on an Azure virtual machine and integrated with a custom domain via AWS Route 53. Caddy is used to manage HTTPS and reverse proxy, while Gunicorn is used as the production WSGI server.

## Project Overview

- Backend: Flask application
- Server: Azure VM (Ubuntu 22.04)
- WSGI: Gunicorn bound to 127.0.0.1:5000
- HTTPS/Proxy: Managed by Caddy
- DNS: api.umexim.com (managed via AWS Route 53)
- CORS: Only allows requests from https://umexim.com

## Endpoints

### GET /api/ping

- Purpose: Simple health check
- Response: `{ "message": "Bamboo Backend Server is OPERATIONAL and here is PONG from backend" }`

### POST /api/message

- Purpose: Accepts a message from the frontend
- Expected input: JSON with a "text" key, e.g. `{ "text": "Hello" }`
- Response: `{ "response": "Bamboo Backend Server is OPERATIONAL and has RECEIVED the following message: Hello" }`

## File Structure

bamboo-backend-flask-api/
├── app.py             # Flask app with /ping and /message routes
├── Caddyfile          # Caddy HTTPS reverse proxy config
├── README.md          # You're reading it!
└── docs/
    ├── curl-ping-success.png
    ├── curl-message-success.png
    ├── browser-message-alert.png
    └── browser-ping-alert.png
