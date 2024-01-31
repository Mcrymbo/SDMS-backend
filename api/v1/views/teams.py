#!/usr/bin/python3
"""serves team data to the api"""

from api.v1.views import app_views
from models.event import Team
from models import storage
from flask import jsonify, make_response, abort, request


@app_views.route('/teams', methods=['GET'], strict_slashes=False)
def get_teams():
	"""get all the teams from db"""
	teams = storage.all('Team').values()
	if len(teams) == 0:
		abort(404)
	team_list = [team.to_dict() for team in teams]

	return jsonify(team_list)

@app_views.route('/teams/<team_id>', methods=['GET'], strict_slashes=False)
def get_team(team_id):
	"""get a team by using the id"""
	team = storage.get(Team, team_id)
	if not team:
		abort(404)
	
	return jsonify(team.to_dict())

@app_views.route('/teams/<team_id>', methods=["DELETE"], strict_slashes=False)
def delete_team(team_id):
	"""delete a team"""
	team = storage.get(Team, team_id)
	if not team:
		abort(404)

	return jsonify(team.to_dict())

@app_views.route('/teams/<team_id>', methods=["DELETE"], strict_slashes=False)
def delete_team(team_id):
	"""delete team from db"""
	team = storage.get(Team, team_id)
	if not team:
		abort(404)

	storage.delete(team)
	storage.save()
	return make_response('Team with id {} deleted'.format(team_id))

@app_views.route('/teams', methods=['POST'], strict_slashes=False)
def add_team():
	"""add a team to the db"""
	data = request.get_json()
	if not data:
		abort(400)

	required_fields = ['name', 'coach_id']

	for field in required_fields:
		if field not in data:
			abort(400, 'Missing {} in the request'.format(field))

		team = Team(**data)
		storage.new(team)
		storage.save()
		return make_response(jsonify(team.to_dict()), 201)
	
@app_views.route('/teams/<team_id>', methods=['PUT'], strict_slashes=False)
def update_team(team_id):
	"""update the details of a team"""
	data = request.get_json()
	if not data:
		abort(400)
	team = storage.get(Team, team_id)
	if not team:
		abort(404)

	ignore = ['id', 'created_at', 'updated_at']
	for key, value in data.items():
		if key not in ignore:
			setattr(team, key, value)

	team.save()
	return make_response(jsonify(team.to_dict()), 200)
