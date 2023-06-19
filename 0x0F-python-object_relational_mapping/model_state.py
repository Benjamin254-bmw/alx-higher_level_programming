#!/usr/bin/python3
"""python file that contains the class definition of
a State and an instance Base = declarative_base():
State class:
    inherits from Base Tips
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string with
    maximum 128 characters and can’t be null
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
