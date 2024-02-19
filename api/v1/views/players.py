#!/usr/bin/python3
"""serves team data to the api"""

from api.v1.views import app_views
from models.player import Player
from models import storage
from flask import jsonify, make_response, abort, request
from flask_jwt_extended import jwt_required


@app_views.route('/players', methods=['GET'], strict_slashes=False)
def get_players():
    """get players from db"""
    players = storage.all(Player).values()
    if len(players) == 0:
    	abort(404)
    player_list = []
    for player in players:
        player_list.append(player.to_dict())

    return jsonify(player_list)

@app_views.route('/players/<player_id>', methods=['GET'], strict_slashes=False)
def get_player(player_id):
    """get one player from db"""
    Player = storage.all(Player, player_id)
    if not Player:
    	abort(404)

    return jsonify(Player.to_dict())

@app_views.route('/players/<player_id>', methods=["DELETE"], strict_slashes=False)
def delete_player(player_id):
    """delete player from db"""
    player = storage.get(Player, player_id)
    if not player:
        abort(404)
    storage.delete(player)
    storage.save()
    return make_response('Player with id {} deleted'.format(player.id))

@app_views.route('/players', methods=['POST'], strict_slashes=False)
def add_player():
    """add a player to the db"""
    data = request.get_json()
    if not data:
        abort(400)
    
    required_fields = ['name', 'is_male', 'team_id', 'coach_id']
    for field in required_fields:
        if field not in data:
            abort(400, description='Missing {} in the request'.format(field))

    player = Player(**data)
    storage.new(player)
    storage.save()
    return make_response(jsonify(player.to_dict()), 201)

@app_views.route('/players/<player_id>', methods=['PUT'], strict_slashes=False)
def update_player(player_id):
    """update the particulars of a player"""
    data = request.get_json()
    if not data:
        abort(400)
    player = storage.get(Player, player_id)
    if not player:
        abort(404)
        
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(player, key, value)
    player.save()
    return make_response(jsonify(player.to_dict()), 200)
