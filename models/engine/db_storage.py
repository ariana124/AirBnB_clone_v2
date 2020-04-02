#!/usr/bin/python3
"""Database storage class"""
import models
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"State": State,
           "City": City}
# "User": User
# "Place": Place,
# "Review": Review,
# "Amenity": Amenity}


class DBStorage:
    """this is the Databse storage
    Attributes:
        __engine: initialize with None
        __session: initialize with None
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instance attribute for DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        obj = {}
        clss = [value for key, value in classes.items()]
        if cls:
            if type(cls) == str:
                cls = classes[cls]
            clss = [cls]
        for one_class in clss:
            for value in self.__session.query(one_class):
                key = str(value.__class__.__name__) + "." + str(value.id)
                obj[key] = value
        return obj

    def new(self, obj):
        """adds objects to current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from the current database session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates the current database session from the engine"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """removes the private session attribute"""
        if self.__session:
            self.__session.remove()
