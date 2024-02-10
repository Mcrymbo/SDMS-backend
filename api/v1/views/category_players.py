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

    female = []
    male = []

    for category in cat_list:
        obj_male = {'name': category['name'], 'players': []}
        obj_female = {'name': category['name'], 'players': []}
        for player in player_list:
            if player['category']['id'] == category['id']:
                mod_player = player.copy()
                del mod_player['category']
                if mod_player['is_male']:
                    mod_player['gender'] = 'male'
                    obj_male['players'].append(mod_player)
                elif mod_player['is_male'] is False:
                    mod_player['gender'] = 'female'
                    obj_female['players'].append(mod_player)

        female.append(obj_female)
        male.append(obj_male)
     
    return {'Male': male, 'Female': female}

@app_views.route('/category_players', methods=['GET'], strict_slashes=False)
def get_category_players():
    """ gets all players of an event in a category """
    
    players = storage.all(Player).values()
    categories = storage.all(Category).values()
    
    data = category_players(players, categories)
    return jsonify(data)

@app_views.route('/events/players', methods=['GET'], strict_slashes=False)
def get_event_players():
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

@app_views.route('/events/category_players', methods=['GET'], strict_slashes=False)
def get_event_category_players():
    """ gets all players of an event """
    events = storage.all(Event).values()
    categories = storage.all(Category).values()
    if len(events) == 0:
        abort(404)
    
    player_list = []
    lst = []

    for event in events:
        cobj = {'Event': event.to_dict()['name'], 'category': []}
        obj = {'event': event.to_dict()['name'], 'players': []}
        players = storage.event_players(event.to_dict()['id'])
        for player in players:
            obj['players'].append(player)

            data = category_players(obj['players'], categories)
            cobj['category'].append(data)
        player_list.append(obj)

        lst.append(cobj)
    return jsonify(lst), 200
