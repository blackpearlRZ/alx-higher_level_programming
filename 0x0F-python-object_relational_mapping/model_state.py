#!/usr/bin/python3
""" Contains the class State """
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class that inherits from Base """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="State",
                          cascade="all, delete-orphan")

    # Getter incase of storage type is FileStorage
    if getenv('HBNB_TYPE_STORAGE') == db:
        @property
        def cities(self):
            from models import storage
            """ getter method that returls list of City instances """
            return [City for Cities in storage.all("City").items()
                    if City.state_id == self.id]
