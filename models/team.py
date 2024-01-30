#!/usr/bin/python3
"""
defines team model
"""
from models.player import Player
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.event import Event


#team_events = Table('team_events', Base.metadata,
#                    Column('team_id', String(60), ForeignKey('teams.id'), primary_key=True),
#                    Column('event_id', String(60), ForeignKey('events.id'), primary_key=True)
#                    )


class Team(BaseModel, Base):
    """ class for creating team table """
    __tablename__ = 'teams'
    name = Column(String(60), nullable=False)
    #events = relationship('Event', secondary=team_events, viewonly=False)
    players = relationship('Player', backref='team')
    coach_id = Column(String(60), ForeignKey('coaches.id', onupdate='CASCADE', ondelete='CASCADE'))


    def __init__(self, *args, **kwargs):
        """ Initialize teams """
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

