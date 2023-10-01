#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


 class Square(Rectangle):
     """Represents a square"""
     
     def __init__(self, size):
        """__init__ method.
        Args:
            size (int): The size of the square.
        """
        
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size ** 2


if __name__ == '__main__':
    
    print(Square)
    print(Square(13).area())
    print(issubclass(Square, Rectangle))
