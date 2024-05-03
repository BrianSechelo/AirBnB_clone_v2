#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Represents a City for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table cities.
    attributes:
    __tablename__(str)" The name of the MySQL table to store cities.
    name (sqlalchemy String): The state id of the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("place", backref="cities", cascade="delete")
