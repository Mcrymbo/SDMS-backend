#!/usr/bin/python3
"""
Base model that defines content shared among all models
"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models

Base = declarative_base()
time_format = '%Y-%m-%dT%H:%M:%S.%f'

class BaseModel:
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        """ Initializing the base class """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ defines string representation of BaseModel """
        class_name = self.__class__.__name___
        return "[{:s}] ({:s}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates updated_at with current time """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, cls=None):
        """ creates a dict object for an instance """
        new_dict = self.__dict__.copy()
        if 'created_at' in new_dict:
            new_dict['created_at'] = new_dict['created_at'].strftime(time_format)
        if 'updated_at' in new_dict:
            new_dict['updated_at'] = new_dict['updated_at'].strftime(time_format)
        new_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """ deletes object from the database """
        models.storage.delete(self)
