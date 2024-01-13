#!/usr/bin/python3
"""Improves the file model_state.py"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative
from sqlalchemy.orm import relatiom=nship

myMetaData = MetaData()
Base = declarative_base(metadata=myMetaData)

class State(Base):
    """class with id and name attributes of each state"""
    __tablename__ = 'states'
    id = Column(Integer,unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable-False)
    cities = relationship("city", backref="states")
