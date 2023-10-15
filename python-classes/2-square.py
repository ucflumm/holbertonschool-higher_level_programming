#!/usr/bin/python3
"""Definition of class Square"""


class Square:
    """
    Class Square with attribute size

    Attributes:
    __size (int): size of the square
    """
    def __init__(self, size=0):
        """ Initialize the square with a given size """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
