#!/usr/bin/python3
"""defines a rectangle class"""
from models.base import Base

class Rectangle(Base):
    """represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=none):
        """initialize a new rectangle

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
                TypeError: If either of width or height is not an int.
                ValueError: If either of width or height <= 0.
                TypeError: If either of x or y is not an int.
                ValueError: If either of x or y < 0.
        """
        self.width = width
        self.hight = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set or get the width of the rectangle"""
        return self.width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
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
