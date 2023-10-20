#!/usr/bin/python3
"""
    Module for Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square class extends Rectangle extends BaseGeometry
        Args:
            size (int): Square size
    """
    def __init__(self, size):
        """
            Instantiation of Square class
        """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """
            Overrides the area() method in BaseGeometry
            Returns area of Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
            Returns string representation of Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
