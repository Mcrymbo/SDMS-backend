#!/usr/bin/python3
"""
defines model for holding coaches
"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models.team import Team
from models.player import Player
from sqlalchemy.orm import relationship

class Coach(BaseModel, Base):
    """ class for defining coach model """
    __tablename__ = 'coaches'
    name = Column(String(60), nullable=False)
    teams = relationship('Team', backref='coach')
    players = relationship('Player', backref='coach')

    def __init__(self, *args, **kwargs):
        """ initializing coach class """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ str method """
        return self.name
