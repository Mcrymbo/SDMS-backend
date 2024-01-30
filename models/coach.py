#!/usr/bin/python3
"""
defines model for holding coaches
"""
from models.participant import Participant
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Coach(BaseModel, Base):
    """ class for defining coach model """
    __tablename__ = 'coaches'
    name = Column(String(60), nullable=False)
    player = relationship('Player',
                                backref='coach',
                                cascade='all, delete, delete-orphan')
