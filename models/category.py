#!/usr/bin/python3
"""
Defines the different categories to e played
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """ class that defines category of the games to be played """
    __tablename__ = "categories"
    name = Column(String(60), nullable=False)
    lower_limit = Column(Integer, nullable=False)
    upper_limit = Column(Integer, nullable=False)
    #players = relationship('Player', backref='category')


    def __init__(self, *args, **kwargs):
        """ Initializes the category class """
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

    def assign_players(self, players):
        """ assign a player """
        from models.player import Player
        for player in players:
            if self.lower_limit <= player.Weight <= self.upper_limit:
                player.category = self
