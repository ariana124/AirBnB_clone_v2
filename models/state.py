#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """ returns a list of associated cities """
            city_list = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
