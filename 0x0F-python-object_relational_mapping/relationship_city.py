#!/usr/bin/python3

"""
    Defines classes for tables
"""
from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    """
    Creates table for cities
    """

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
