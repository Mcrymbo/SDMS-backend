#!/usr/bin/python3
"""serves events data to the api"""

from api.v1.views import app_views
from models.event import Event
from models import storage
from flask import jsonify, make_response, abort, request


@app_views.route('/events', methods=['GET'], strict_slashes=False)
def get_events():
	"""get events from db"""
	events = storage.all('Event').values()
	if len(events) == 0:
		abort(404)
	event_list = [event.to_dict() for event in events]
	return jsonify(event_list)

@app_views.route('events/<event_id>', methods=['GET'], strict_slashes=False)
def get_event(event_id):
	"""get an event using an id"""
	event = storage.get(Event, event_id)
	if not event:
		abort(404)
	return jsonify(event.to_dict)

@app_views('events/<event_id>', methods=['DELETE'], strict_slashes=False)
def delete_event(event_id):
	"""delete an event from db"""
	event = storage.get(Event, event_id)
	if not event:
		abort(404)
	storage.delete(event)
	storage.save()

	return make_response('Event with id {} deleted'.format(event.id))

@app_views('/events', methods=['POST'], strict_slashes=False)
def add_event():
	"""adds an event to the db"""
	data = request.get_json()
	if not data:
		abort(400)

	if 'name' not in data:
		abort(400, description="Missing name")

	event = Event(**data)
	storage.new(event)
	storage.save()
	return make_response(jsonify(event.to_dict), 201)

@app_views.route('/events/<event_id>', methods=['PUT'], strict_slashes=False)
def update_event(event_id):
	"""update an event in the db using an id"""
	data  = request.get_json()
	if not data:
		abort(400)
	event = storage.get(Event, event_id)
	if not event:
		abort(404)

	ignore = ['id', 'created_at', 'updated_at']

	for key, value in data.items():
		if key not in ignore:
			setattr(event, key, value)

	event.save()
	return make_response(jsonify(event.to_dict()), 200)