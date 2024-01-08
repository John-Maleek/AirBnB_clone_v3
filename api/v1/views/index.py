#!/usr/bin/python3
"""
Module defines routes for app_views
"""

from flask import jsonify
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models import storage


@app_views.route('/status', strict_slashes=False)
def app_status():
    return (jsonify({"status": "OK"}))


@app_views.route("/stats", strict_slashes=False)
def app_stats():
    res_object = {"amenities": storage.count(Amenity),
                  "cities": storage.count(City),
                  "places": storage.count(Place),
                  "reviews": storage.count(Review),
                  "states": storage.count(State),
                  "users": storage.count(User)}
    return (jsonify(res_object))
