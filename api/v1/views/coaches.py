#!/usr/bin/python3
"""serves team data to the api"""

from api.v1.views import app_views
from models.coach import Coach
from models import storage
from flask import jsonify, make_response, abort, request

@app_views.route('/coaches', methods=['GET'], strict_slashes=False)
def get_coaches():
	"""get coaches from db"""
	coaches = storage.all('coach').values()
	if len(coaches) == 0:
		abort(404)
	coach_list = [coach.to_dict() for coach in coaches]

	return jsonify(coach_list)

@app_views.route('/coaches/<coach_id>', methods=['GET'], strict_slashes=False)
def get_coach(coach_id):
	""" Get a coach from db with id"""
	coach = storage.get(Coach, coach_id)
	if not coach:
		abort(404)
	return jsonify(coach.to_dict())

@app_views.route('/coaches/<coach_id>', methods=["DELETE"], strict_slashes=False)
def delete_coach(coach_id):
	"""delete a  coach from db"""
	coach = storage.get(Coach, coach_id)
	if not coach:
		abort(404)
	storage.delete(coach)
	storage.save()

	return make_response('Coach with id {} deleted'.format(coach.id))

@app_views.route('/coaches', methods=['POST'], strict_slashes=False)
def add_coach():
	"""add a coach to the db"""
	data = request.get_json()
	if not data:
		abort(400)
	
	if 'name' not in data:
		abort(400, description="Missing name in the request")

	coach = Coach(**data)
	storage.new(coach)
	storage.save()
	return make_response(jsonify(coach.to_dict()), 201)

@app_views.route('/coaches/<coach_id>', methods=['PUT'], strict_slashes=False)
def update_coach(coach_id):
	"""update the particulars of a coach"""
	data = request.get_json()
	if not data:
		abort(400)
	coach = storage.get(Coach, coach_id)
	if not coach:
		abort(404)

	ignore = ['id', 'created_at', 'updated_at']
	for key, value in data.items():
		if key not in ignore:
			setattr(coach, key, value)
	coach.save()
	return make_response(jsonify(coach.to_dict()), 200)