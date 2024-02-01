#!/usr/bin/python3
"""
model for storing tokens
"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String

class Token(BaseModel, Base):
    """ class that implements TokenList class """
    __tablename__ = 'tokens'
    token = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """ initializes Token class """
        super().__init__(*args, *kwargs)
