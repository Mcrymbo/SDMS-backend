#!/usr/bin/python3
"""
defines index route
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ displays the status of the api """
    return jsonify({"status" : "OK"})
