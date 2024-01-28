#!/usr/bin/python3
"""
model for defining user table
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


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

