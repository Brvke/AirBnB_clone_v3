#!/usr/bin/python3
"""
Index view for API v1
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/status', methods=['GET'])
def status():
    """
    Returns the status of the API
    """
    return jsonify({"status": "OK"})

def get_No_objects():
    """Retrieve the number of each object type"""
    stats = {
        "states": storage.count(State),
        "cities": storage.count(City),
        "users": storage.count(User),
        "reviews": storage.count(Review),
        "amenties": storage.count(Amenity),
        "places": storage.count(Place)
    }
    return jsonify(stats)

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieves the number of each objects by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
