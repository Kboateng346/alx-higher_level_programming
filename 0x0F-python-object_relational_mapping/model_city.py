#!/usr/bin/python3
"""
City module

Contains the City class that inherits from Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from model_state import Base


class City(Base):
    """
    This class links to the `cities` table.

    Attributes:
        id (int): city id.
        name (str): city name.
        state_id (int): id of the state is associated to.
    """

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
