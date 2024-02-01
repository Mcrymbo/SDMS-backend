#!/usr/bin/python3
""" Flask app for manipulating admin panel """
from flask import Flask
from flask_admin import Admin
from models.user import User
from models.event import Event
from models.player import Player
from models.team import Team
from models.coach import Coach
from models import storage
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import RadioField
import uuid


app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
app.config['SECRET_KEY'] = 'mysecret_key'


class UserAdmin(ModelView):
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.id = str(uuid.uuid4())

class EventAdmin(ModelView):
    column_list = ['name', 'users']
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.id = str(uuid.uuid4())


class PlayerAdmin(ModelView):
    """ adds player as inline model"""
    column_display_pk = True
    column_hide_backrefs = False
    column_list = ['name', 'Weight', 'age', 'events']
    """column_list = [c_attr.key for c_attr in inspect(Player).mapper.column_attrs] """
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.id = str(uuid.uuid4())

class TeamAdmin(ModelView):
    column_list = ['name', 'coach']
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.id = str(uuid.uuid4())

class CoachAdmin(ModelView):
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.id = str(uuid.uuid4())

admin = Admin(app, name='Admin Panel')

admin.add_view(UserAdmin(User, storage.reload()))
admin.add_view(EventAdmin(Event, storage.reload()))
admin.add_view(PlayerAdmin(Player, storage.reload()))
admin.add_view(TeamAdmin(Team, storage.reload()))
admin.add_view(CoachAdmin(Coach, storage.reload()))


if __name__ == '__main__':
    """ runs Flask app """
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
