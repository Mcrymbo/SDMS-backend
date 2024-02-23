#!/usr/bin/python3
"""
Implements storage using mysql
"""
import models
from models.base_model import Base, BaseModel
from models.user import User
from models.event import Event
from models.player import Player, event_players
from models.team import Team
from models.coach import Coach
from models.category import Category
from models.roles import Roles
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {'User': User, 'Event': Event, 'Player': Player, 'Team': Team, 'Coach': Coach, 'Category': Category, 'Roles': Roles}


class DBStorage:
    """
    connects to mysql database
    """
    __engine = None
    __session = None

    def __init__(self):
        """ instantiate DBStorage """
        SDMS_USER = getenv('SDMS_USER')
        SDMS_PWD = getenv('SDMS_PWD')
        SDMS_HOST = getenv('SDMS_HOST')
        SDMS_DB = getenv('SDMS_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(SDMS_USER,
                                              SDMS_PWD,
                                              SDMS_HOST,
                                              SDMS_DB))

    def new(self, obj):
        """ add new item to database """
        self.__session.add(obj)
    
    def connect(self):
        """ used to connect to the database """
        self.__session
    
    def save(self):
        """ saves newobject to the database """
        self.__session.commit()

    def all(self, cls=None):
        """ query database session """
        new_dict = {}
        for clas in classes:
            if cls is None or cls is classes[clas] or cls is clas:
                objs = self.__session.query(classes[clas]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def reload(self):
        """ reloads data from the database """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess_factory)
        self.connect = self.__session
        return self.__session

    def close(self):
        """ closes database """
        self.__session.remove()

    def get(self, cls, id):
        """ get object stored in a database """
        if cls not in classes.values():
            return None

        data = models.storage.all(cls)
        for value in data.values():
            if (value.id == id):
                return value
        return None

    def delete(self, obj=None):
        """ delete object from storage """
        if obj is not None:
            self.__session.delete(obj)

    def event_players(self, event_id):
        return self.__session.query(Player) \
            .join(event_players) \
            .filter(event_players.c.event_id == event_id) \
            .all()

    def user_role(self, role_id):
        """ assigns role to a user """
        return self.__session.query(User) \
                .join(user_roles) \
                .filter(user_roles.c.user_id == role_id) \
                .all()
