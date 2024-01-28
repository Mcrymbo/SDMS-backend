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

classes = {'User': User}


class DBStorage:
    """
    connects to mysql database
    """
    __engine = None
    session = None

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

    def save(self):
        """ saves newobject to the database """
        self.session.commit()

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
        self.session = scoped_session(sess_factory)

    def close(self):
        """ closes database """
        self.session.remove()

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
            self.session.delete(obj)
