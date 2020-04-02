#!/usr/bin/python3
"""
Database storage class
"""

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from slqalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """ handles storage for database """
    __engine = None
    __session = None
    __classes = {"Amenity": Amenity, "City": City, "Place": Place,
                 "Review": Review, "State": State, "User": User}

    def __init__(self):
        """ creates the engine self.__engine """
        user = os.environ.get("HBNB_MYSQL_USER")
        passwd = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        db = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == test:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session """


    def new(self, obj):
        """ adds objects to current database session """
        self.__session.add(obj)

    def save(self):
        """ commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes obj from the current database session if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ creates the current database session from the engine """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ removes the private session attribute """
        self.__session.remove()
