#!/usr/bin/python3

"""
    script that defined a MySQL table model `State` using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State defines a model for a MySQL DB table 'states'

    Args:
        Base: Base class from which all mapped models must inherit
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=128), nullable=False)
