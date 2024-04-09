#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv


place_amenities = Table("place_amenity", Base.metadata,
                        Column("place_id", String(60), ForeignKey("places.id"),
                               primary_key=True, nullable=False),
                        Column("amenities_id", String(60),
                               ForeignKey("amenities.id"),
                               primary_key=True, nullable=False)
                        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review",
                               cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            res = storage.all()
            lst = []
            result = []
            for x in res.keys():
                x = x.split('.')[0]
                if x == 'Review':
                    lst.append(res[x])

            for t in l:
                if t.place_id == self.id:
                    result.append(t)

            return r

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
