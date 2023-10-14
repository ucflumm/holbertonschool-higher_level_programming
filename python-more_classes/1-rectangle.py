#!/usr/bin/python3
"""Module 0-rectangle.py"""


class Rectangle:
    """Class rectangle with private attributes width and height"""
    def __init__(self, width=0, height=0):
        """assign each arguments width and height to each attribute"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """return value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """return value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
