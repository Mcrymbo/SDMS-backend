#!/usr/bin/python3
"""
serves users to the api
"""
from api.v1.views import app_views
from models.user import User
from models import storage
from flask import jsonify, make_response


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """ Get users from the database """
    users = storage.get('User').all()
    user_list = []
    for user in users:
        user_list.append(user)

    return user_list

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def user(user_id):
    if not user_id:
        return jsonify({'User': 'No user'})
    user = storage.get('User', user_id)
    return make_response(jsonify(user), 200)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def add_user


