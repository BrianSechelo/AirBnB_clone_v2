#!/usr/bin/python3
import os
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import object_session

class DBStorage:
    """Class to manage database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}', pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
        self.reload()
    def all(self, cls=None):
        """Query all objects depending on the class name (or all types if cls is None)"""
        if cls:
            return self.__session.query(cls).all()
        else:
            return {obj.__class__.__name__ + '.' + obj.id: obj for obj in self.__session.query(Base)}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    def close(self):
        """Close the working SQLALCHEMY session"""
        self.__session.close()
