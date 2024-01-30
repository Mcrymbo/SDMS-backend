#!/usr/bin/python3
"""
model for defining user table
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5


class User(BaseModel, Base):
    """ defines users table """
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    phone_number = Column(String(12), nullable=True)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """ initializing the user class """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """ sets password with md5 encription """
        if name == 'password':
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def __str__(self):
        """ defines string representation """
        return "{}".format(self.first_name)
