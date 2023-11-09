#!/usr/bin/python3
"""my module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """my square class"""

    def __init__(self, size):
        """instantiation function"""
        super().integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """area function"""
        return self.__size ** 2
    
    def __str__(self):
        """return string for print"""
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
