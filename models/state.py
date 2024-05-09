#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
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
        for key, val in models.storage.all().items():
            if key == self.__name__ + "." + self.id:
                ct.append(val)
        return ct
