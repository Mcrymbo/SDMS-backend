#!/usr/bin/python3
"""
Implements storage using mysql
"""
import models
from models.base_model import Base, BaseModel
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """
    connects to mysql database
    """
    __engine = None
    __session = None

    def __init__(self):
        """ instantiate DBStorage """
        APP_USER = getenv('APP_USER')
        APP_PWD = getenv('APP_PWD')
        APP_HOST = getenv('APP_HOST')
        APP_DB = getenv('APP_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(APP_USER, APP_PWD, APP_HOST, APP_DB))

    def new(self, obj):
        """ add new item to database """
        self.__session.add(obj)

    def save(self):
        """ saves newobject to the database """
        self.__session.commit()

    def reload(self):
        """ reloads data from the database """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess_factory)

    def close(self):
        """ closes database """
        self.__session.remove()
