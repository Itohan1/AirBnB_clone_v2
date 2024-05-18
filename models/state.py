#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os

storage_type = os.getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    def __init__(self):
        """"""
        super().__init__()

    #from models.__init__.py import storage
    if self.storage.__class__.__name__ == 'DBStorage':
        cities = relationship("City", cascade="all, delete", backref="state")
    elif self.storage.__class__name == 'FileStorage':
        @property
        def cities(self):
            """"""

            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
