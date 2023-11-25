#!/usr/bin/python3
"""defines a base class model"""

class Base:
    """base class that represents the base for all other classes.
    private Class attribute:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """initialize a new base.
        Args:
            id (int): identity of the new base.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
