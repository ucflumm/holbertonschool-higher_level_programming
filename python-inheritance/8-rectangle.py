#!/usr/bin/python3
"""
    Module for Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle class extends BaseGeometry
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
