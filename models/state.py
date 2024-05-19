#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        ct = []
        for key, val in models.storage.all(City).items():
            if val.state_id == self.id:
                ct.append(val)
        return ct
