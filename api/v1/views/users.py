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
    """ gets a user """
    user = storage.get(User, user_id)

    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """ delte a user from database """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return make_response('user with id {} deleted'.format(user.id))

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

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ updates a paricular user """
    data = request.get_json()
    if not data:
        abort(400)
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    ignore = ['id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
