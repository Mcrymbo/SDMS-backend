#!/usr/bin/python3
"""
defines api endpoints for category class
"""
from models.category import Category
from api.v1.views import app_views
from models import storage
from flask import make_response, jsonify, abort, request


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def categories():
    """ gets all categories """

    categories = storage.all('Category').values()
    if len(categories) == 0:
        abort(404)

    cat_all = []
    for category in categories:
        cat_all.append(category.to_dict())

    return jsonify(cat_all), 200

@app_views.route('/categories/<cat_id>', methods=['GET'], strict_slashes=False)
def category(cat_id):
    """ cat one category of specifi id """
    category = storage.get(Category, cat_id)
    if not category:
        abort(404)

    return jsonify(category.to_dict()), 200

@app_views.route('categories', methods=['POST'], strict_slashes=False)
def post_category():
    """ add a category """
    data = request.get_json()
    if not data:
        abort(404, description='Not a json')

    fields = ['name','lower_limit', 'upper_limit']
    for field in fields:
        if field not in data:
            abort(400, description='Missing {}'.format(field))

    category = Category(**data)
    category.save()

    return jsonify(category.to_dict()), 201

@app_views.route('categories/<cat_id>', methods=['DELETE'], strict_slashes=False)
def delete_category(cat_id):
    """ deleltes a category """
    category = storage.get(Category, cat_id)
    if not category:
        abort(404)

    storage.delete(category)
    storage.save()
    return make_response(jsonify({'message': '{} category deleted successfuly'.format(category.to_dict()['name'])}))

