#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship("City", cascade="delete")
    else:
        @property
        def cities(self):
            """Returns cities obj
            """
            newlist = []
            r =  models.storage.all(City)
            for key, value in r.items():
                if 'state_id' in value:
                    if value[state_id] == self.id:
                        newlist.append(value)
            return (newlist)
