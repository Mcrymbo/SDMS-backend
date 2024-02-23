#!/usr/bin/python3
"""
model for creating event
"""
from sqlalchemy import Column, String, ForeignKey, Table
from models.base_model import BaseModel, Base
from models.category import Category
from models.user import User
from sqlalchemy.orm import relationship


event_users = Table('event_users', Base.metadata,
                    Column('user_id', String(60),
                           ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE')),
                    Column('event_id', String(60),
                           ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'))
                    )


class Event(BaseModel, Base):
    """ class for creating event model """
    __tablename__ = 'events'
    name = Column(String(50), nullable=False, unique=True)
    users = relationship('User', secondary=event_users, viewonly=True, backref='event')
    categories = relationship('Category', backref='events')

    def __init__(self, *args, **kwargs):
        """ initializes Event class """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ str method """
        return self.name
