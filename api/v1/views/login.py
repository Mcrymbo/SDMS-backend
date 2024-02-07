#!/usr/bin/python3
"""
handles the login onto the application and sets up security using jwt
"""
from api.v1.views import app_views
from models.user import User
from models import storage
from flask import jsonify, make_response, request, abort
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash


def check_password(user_password, data_password):
    return check_password_hash(user_password, data_password)


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """ function to login the user """
    data = request.get_json()
    if not data:
        abort(400, description='Not json')
    
    required_fields = ['email', 'password']
    for field in required_fields:
        if field not in data:
            abort(400, description='Missing {} in the response'.format(field))

    user = User.get_user(data['email']).to_dict()

    if user and (check_password(user['password'], data['password'])):
        access_token = create_access_token(identity=user['id'])
        refresh_token = create_refresh_token(identity=user['id'])
        return jsonify({
                        'message': 'Welcome {} {}'.format(user['first_name'], user['last_name']),
                        'access_token': access_token,
                        'refresh_token': refresh_token
                        }), 201
    return jsonify({'error': 'invalid email or password'}), 401
