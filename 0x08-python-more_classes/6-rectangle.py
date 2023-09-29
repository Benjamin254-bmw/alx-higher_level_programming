#!/usr/bin/python3


class Rectangle:
     """Rectangle class.
    Attributes:
        number_of_instances (int): number of rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
       """__init__ method.
        Args:
            width (int): integer width
            height (int): integer height
        """
        
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width: returns width
        Args:
            width (int): integer width
        Returns:
            rectangle width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        return self.__width

    @width.setter
    def width(self, width):
        """set width of rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height: returns height
        Args:
            height (int): integer height
        Returns:
            rectangle height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        return self.__height
i

    @height.setter
    def height(self, height):
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
        """String representation (#) of rectangle.
        Returns:
            string rep of rectangle
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
        Rectangle.number_of_instances -= 1


