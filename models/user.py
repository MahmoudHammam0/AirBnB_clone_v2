#!/usr/bin/python3
""" User class """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from os import getenv


class User(BaseModel, Base):
    """ class User that inherits from BaseModel """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
         email = ""
         password = ""
         first_name = ""
         last_name = ""
