#!/usr/bin/python3
"""
defines blueprint for API
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.login import *
from api.v1.views.coaches import *
from api.v1.views.teams import *
from api.v1.views.players import *
from api.v1.views.events import *
