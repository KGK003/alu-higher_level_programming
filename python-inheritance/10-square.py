#!/usr/bin/python3
"""class Square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inherits from rectangle"""

    def __init__(self, size):
        """set size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of square"""
        a = self.__size * self.__size
        return a

    def __str__(self):
        """return [Square] <width>/<height>"""
        return super().__str__()
