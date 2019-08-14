#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # cities = relationship("City", cascade="delete")
    cities = relationship('City', backref='state')

    @property
    def cities(self):
        """Returns cities obj
        """
        newlist = []
        for city in self.cities:
            if city.state_id == self.id:
                newlist.append(city)
        return (newlist)
