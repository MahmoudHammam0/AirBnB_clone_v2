#!/usr/bin/python3
""" User class """
from sqlalchemy import Column, String, event
from models.base_model import BaseModel, Base
import hashlib


class User(BaseModel, Base):
    """ class User that inherits from BaseModel """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    _password = Column('password', String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    @property
    def password(self):
        """Getter method for password"""
        return self._password

    @password.setter
    def password(self, value):
        """Setter method for password that automatically hashes the value"""
        self._password = hashlib.sha256(value.encode()).hexdigest()
