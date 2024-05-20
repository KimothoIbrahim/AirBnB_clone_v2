#!/usr/bin/python3
"""make sql database """
from sqlalchemy import create_engine
from os import getenv
from models.city import City
from models.state import State
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ database engine """
    __engine = None
    __session = None

    def __init__(self):
        """ setup engine """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ retrieve averythiing """
        dic = {}

        if cls:
            if type(cls) == str:
                cls = eval(cls)
            res = self.__session.query(cls)
            for eachObject in res:
                key = type(eachObject).__name__ + '.' + eachObject.id
                dic.update({key: eachObject})
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for clas in classes:
                res = self.__session.query(clas).all()
                for eachObject in res:
                    key = type(eachObject).__name__ + '.' + eachObject.id
                    dic.update({key: eachObject})
        return dic

    def new(self, obj):
        """ add a new object """
        self.__session.add(obj)

    def save(self):
        """ save method """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete method """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ helpers """
        Base.metadata.create_all(self.__engine)
        preSession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(preSession)
        self.__session = Session()

    def close(self):
        """
        method on the private session attribute (self.__session) tips
        or close() on the class Session tips
        """
        self.__session.close()
