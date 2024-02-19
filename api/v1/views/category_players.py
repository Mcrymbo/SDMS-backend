#!/usr/bin/python3
"""
gets all the players of a given category
"""
from api.v1.views import app_views
from models import storage
from models.player import Player, event_players
from models.event import Event
from models.category import Category
from flask import jsonify, abort, make_response


def category_players(players, categories):
    """ gets all players of a given category """
    
    if len(players) == 0 or len(categories) == 0:
        abort(404)
    
    cat_list = []
    for category in categories:
        category.assign_players(players)
        cat_list.append(category.to_dict())
    
    player_list = []
    for player in players:
        player.category = player.category.to_dict()
        player_list.append(player.to_dict())

    data = []

    for category in cat_list:
        obj = {'name': category['name'], 'players': []}
        for player in player_list:
            if player['category']['id'] == category['id']:
                mod_player = player.copy()
                del mod_player['category']
                obj['players'].append(mod_player)

        data.append(obj)
     
    return data

def cat_players(players, category_id):
    """ gets all players of a given category """

    categories = storage.all(Category).values()
    
    if len(players) == 0:
        abort(404)

    cat_list = []
    for category in categories:
        category.assign_players(players)
        cat_list.append(category.to_dict())
    
    player_list = []
    for player in players:
        player.category = player.category.to_dict()
        if player.category['id'] == category_id:
            player_list.append(player.to_dict())
         
    return jsonify(player_list) 

@app_views.route('/events/players', methods=['GET'], strict_slashes=False)
def get_events_players():
    """ gets all players of an event """
    events = storage.all(Event).values()
    if len(events) == 0:
        abort(404)
    
    player_list = []

    for event in events:
        obj = {'event': event.to_dict()['name'], 'players': []}
        players = storage.event_players(event.to_dict()['id'])
        for player in players:
            obj['players'].append(player.to_dict())

        player_list.append(obj)
    
    return jsonify(player_list), 200

@app_views.route('/events/<event_id>/players', methods=['GET'], strict_slashes=False)
def get_event_players(event_id):
    """ gets all players of an event """
    event = storage.get(Event, event_id)
    if not event:
        abort(404)
    
    male = []
    female = []
    players = storage.event_players(event.to_dict()['id'])
    for player in players:
        if player.to_dict()['is_male']:
            male.append(player.to_dict())
        else:
            female.append(player.to_dict())
    
    return jsonify({'Female': female, 'Male': male}), 200

@app_views.route('/events/<event_id>/category_players', methods=['GET'], strict_slashes=False)
def get_event_cat_players(event_id):
    """ gets all players of an event """
    event = storage.get(Event, event_id)
    categories = storage.all(Category).values()
    if not event:
        abort(404)
    
    male = []
    female = []
    players = storage.event_players(event.to_dict()['id'])
    for player in players:
        if player.to_dict()['is_male']:
            male.append(player)
        else:
            female.append(player)

    male = category_players(male, categories)
    female = category_players(female, categories) 

    female_data = [category for category in female if len(category['players']) > 0]
    male_data = [category for category in male if len(category['players']) > 0 ]

    return jsonify({'Female': female_data, 'Male': male_data}), 200

@app_views.route('/events/<event_id>/categories/<cat_id>/players', methods=['GET'], strict_slashes=False)
def get_event_single_cat_players(event_id, cat_id):
    """ gets all players of an event """
    event = storage.get(Event, event_id)
    #categories = storage.get(Category, cat_id)
    if not event:
        abort(404)
    
    male = []
    female = []
    players = storage.event_players(event.to_dict()['id'])
    for player in players:
        if player.to_dict()['is_male']:
            male.append(player.to_dict())
        else:
            female.append(player.to_dict())

    #male_data = cat_players(male, cat_id)
    #female_data = cat_players(female, cat_id) 

    #female_data = [category for category in female if len(category['players']) > 0]
    #male_data = [category for category in male if len(category['players']) > 0 ]

    return jsonify({'Female': female, 'Male': male}), 200


