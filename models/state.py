#!/usr/bin/python3
""" State module """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.city import City
import models


class State(BaseModel):
    """ state class that inherits from BaseModel """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """Getter attribute that returns the list of City instances"""
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
