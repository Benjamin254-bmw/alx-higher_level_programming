#!/usr/bin/python3
"""Initializes a rectangle """

class Rectangle:
    """Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height
i

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return the printable representation of the rectangle
        using the character '#' 
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for i in range(self.__height):
            [shape.append('#') for k in range(self.__width)]
            if i != self.__height -1:
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """return the string representation of the rectangle"""
        shape = "Rectangle(" + str(self.__width)
        shape += ", " + str(self.__heigth) + ")"
        return(shape) 
    def __del__(self):
        """print a message for every deletion of a Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

