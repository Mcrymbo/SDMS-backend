#!/usr/bin/pytho3
"""
model that defines user roles
"""
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy.orm import relationship


user_roles = Table('user_roles', Base.metadata,
                   Column('roles_id', String(60), ForeignKey('roles.id', onupdate='CASCADE', ondelete='CASCADE')),
                   Column('users_id', String(60), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE')))


class Roles(BaseModel, Base):
    """ class that defines roles model """
    __tablename__ = 'roles'
    name = Column(String(20), nullable=False)
    weight = Column(Integer, nullable=False)
    users = relationship('User', secondary=user_roles, viewonly=False, backref='role')

    def __init__(self, *args, **kwargs):
        """ initializes roles class """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ defines string representation of the model """
        return self.name
