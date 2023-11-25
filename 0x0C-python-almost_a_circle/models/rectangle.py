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
        """private instance attribut setter"""
        self.__width = value

    @propery
    def height(self):
        """private instance attribute getter"""
        return self.height

    @height.setter
    def height(self, value):
        """private instance attribute setter"""
        self.__height = value

    @property
    def x(self):
        """private instance attribute getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """private instance attribute setter"""
        self.__x = value

    @property
    def y(self):
        """private instance attribute getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """private instance attribute setter"""
        self.__y = value
