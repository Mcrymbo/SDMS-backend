#!/usr/bin/python3
"""
Base model that defines content shared among all models
"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class BaseModel:
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datatime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self):
        """ Initializing the base class """
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
