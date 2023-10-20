#!/usr/bin/python3
"""
    Module for Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle extends BaseGeometry
        Args:
            width (int): Rectangle width
            height (int): Rectangle height
    """
    def __init__(self, width, height):
        """
            Instantiation of Rectangle class
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """
            Overrides the area() method in BaseGeometry
            Returns area of Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
            Returns string representation of Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
