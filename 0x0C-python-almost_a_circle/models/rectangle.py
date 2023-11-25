#!/usr/bin/python3
"""my class module."""
from models.base import Base

class Rectangle(Base):
    """my Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=none):
        """class constructor"""

        self.width = width
        self.hight = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """private instance attribute getter"""
        return self.width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width: must be > 0")
        self.__height = value

    @property
    def x(self):
        """set or get the x coordinates of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """set or get the y coordinates of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
