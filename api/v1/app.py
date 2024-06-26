#!/usr/bin/python3
"""
Flask application
"""
from flask import Flask, jsonify
from os import environ
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(exception=None):
    """
    Closes the storage on app context teardown
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors that returns a JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    import os
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
