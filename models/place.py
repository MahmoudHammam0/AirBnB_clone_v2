#!/usr/bin/python3
""" Place module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
import models


class Place(BaseModel, Base):
    """ Place class that inherits from BaseModel """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete-orphan",
                           backref='place')
    place_amenity = Table('place_amenity', Base.metadata,
                            Column('place_id',
                                   String(60), ForeignKey('places.id'),
                                   primary_key=True, nullable=False),
                            Column('amenity_id',
                                   String(60), ForeignKey('amenities.id'),
                                   primary_key=True, nullable=False))
    amenities = relationship("Amenity", secondary='place_amenity',
                             viewonly=False, backref="places")

    def __init__(self, *args, **kwargs):
        '''Place initialization'''
        super().__init__(*args, **kwargs)
        self.amenity_ids = []

    @property
    def reviews(self):
        '''getter method for reviews relationship with place'''
        objects = storage.all()
        res_list = []
        for key, value in objects.items():
            if value.place_id == self.id:
                res_list.append(value)
        return res_list

    @property
    def amenities(self):
        '''getter method for amenities'''
        objs = storage.all()
        amen_list = []
        for key, value in objs.items():
            if (value.place_id == self.id):
                amen_list.append(value)
        return amen_list

    @amenities.setter
    def amenities(self, obj):
        '''setter method to populate amenity_ids attribute'''
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
