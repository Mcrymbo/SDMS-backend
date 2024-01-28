#!/usr/bin/python3
"""
serves users to the api
"""
from api.v1.views import app_views
from models.user import User
from models import storage
from flask import jsonify, make_response, abort, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """ Get users from the database """
    users_a = storage.all('User').values()
    if len(users_a) == 0:
        abort(404)
    user_list = []
    for user in users_a:
        user_list.append(user.to_dict())

    return jsonify(user_list)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def user(user_id):
    if not user_id:
        return jsonify({'User': 'No user'})
    user = storage.get('User', user_id)
    return make_response(jsonify(user.to_dict()), 200)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def add_user():
    """ adds a user to the database """
    data = request.get_json()
    if not data:
        abort(400)

    required_fields = ['email', 'password', 'first_name', 'last_name']
    for field in required_fields:
        if field not in data:
            abort(400, description='missing {} in the request'.format(field))

    user = User(**data)
    storage.new(user)
    storage.save()
    return make_response(jsonify(user.to_dict()), 201)
