#!/usr/bin/python3
"""
route for defining user roles
"""
from api.v1.views import app_views
from models.roles import Roles
from models.user import User
from models import storage
from flask import jsonify, abort, request


@app_views.route('/roles', methods=['GET'], strict_slashes=False)
def get_roles():
    """ gets all roles """
    roles = storage.all(Roles).values()
    if len(roles) == 0:
        abort(404)

    role_list = [ role.to_dict() for role in roles ]
    return jsonify(role_list), 200

@app_views.route('/roles/<role_id>', methods=['GET'], strict_slashes=False)
def get_role(role_id):
    """ get a single user """
    role = storage.get(Roles, role_id)
    if not role:
        abort(404)
    return jsonify(role.to_dict())

@app_views.route('/roles/<role_id>', methods=['DELETE'], strict_slashes=False)
def delete_role(role_id):
    """ delete a role """
    role = storage.get(Roles, role_id)
    if not role:
        abort(404)

    storage.delete(role)
    storage.save()

    return jsonify({'message': 'deleted successfully'}), 200

@app_views.route('/roles', methods=['POST'], strict_slashes=False)
def add_role():
    """ post a role """
    data = request.get_json()
    if not data:
        abort(400, description='not a json')

@app_views.route('/users/roles', methods=['POST'], strict_slashes=False)
def assign_role():
    """ used to assign a role to a user """
    data = request.get_json()
    if not data:
        abort(400, description='not a json')

    fields = ['email', 'role']
    for field in fields:
        if field not in data:
            abort(400, description='missing {}'.format(field))

    roles = storage.all(Roles).values()
    role_exists = any(role.to_dict()['name'] == data['role'] for role in roles)
    if not role_exists:
        abort(400, description='Role {} not found'.format(data['role']))
    user = User.get_user(data['email'])
    if not user:
        return jsonify({'msg': 'user not found'})

    role = next((role for role in roles if role.to_dict()['name'] == data['role']), None)
    if role:
        user.role.append(role)
        #storage.save()
        return jsonify(user.to_dict())
    else:
        abort(400, description='Role {} not found'.format(data['role']))
