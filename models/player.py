#!/usr/bin/python3
"""
defines participants model
"""
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Boolean, Float
from models.event import Event
from models.category import Category
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


event_players = Table('event_players', Base.metadata,
                      Column('player_id', String(60), ForeignKey('players.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
                      Column('event_id', String(60), ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))


class Player(BaseModel, Base):
    """ class for creating particpant model """
    __tablename__ = 'players'
    events = relationship('Event', secondary=event_players, viewonly=False)
    name = Column(String(60), nullable=False)
    Weight = Column(Float, nullable=True)
    age = Column(Integer, nullable=True)
    is_male = Column(Boolean, nullable=False)
    team_id = Column(String(60), ForeignKey('teams.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    coach_id = Column(String(60), ForeignKey('coaches.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    def __init__(self, *args, **kwargs):
        """ initializes player class """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ str method """
        return self.name
