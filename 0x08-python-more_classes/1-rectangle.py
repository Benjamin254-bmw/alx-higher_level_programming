#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """__init__ method initializes instance variables
        Args:
            __width: private instance attribute, width of rectangle
            __height: private instance attribute, height of rectangle
        """
        self.width = width
        self.eight = height

    @property
    def width(self):
        """@property decorates getter function width
        to access private variable width value
        Return:
            return __width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """@width setter decorates setter function width
        to assign private variable __width value
        Raise:
            TypeError: width must be an integer
            ValueError: width must be >= 0"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """@property decorates getter function height
        to access private variable height value
        Return:
            return __height value"""
        return self.__height

    @height.setter
    def hight(self, value):
        """@height setter decorates setter function height
        to assign private variable __height value
        Raise:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height mus be >= 0')
        self.__height = value
