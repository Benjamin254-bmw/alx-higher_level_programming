#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol: any = '#'
    def __init__(self, width=0, height=0):
        """__init__ method initializes instance variables
        Args:
            __width: private instance attribute, width of rectangle
            __height: private instance attribute, height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """@property decorates getter function height
        to access private variable height value
        Return:
            return __height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """@height setter decorates setter function height
        to assign private variable __height value
        Raise:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height mus be >= 0')
        else:
            self.__height = value

    def area(self):
        """public method area() calculates the area of the rectangle
        Return:
            return the rectangle area
        """
        return self.__width*self.__height

    def perimeter(self):
        """public method perimeter() calculates the perimeter of the rectangle
        Return:
            return the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """method __str__ prints the rectangle with character '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        draw = ""
        for row in range(self.__height):
            for col in range(self.__width):
                try:
                    draw += str(self.print_symbol)
                except Exception:
                    draw += type(self.print_symbol)
            if row < self.__height -1:
                draw += '\n'
        return (draw)

    def __del__(self):
        """method __del__ prints a message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method def bigger_or_equal returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method square returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
