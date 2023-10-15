#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """
    Represents a square.

    Attributes:
    __size (int): the size of the square
    """
    def __init__(self, size=0):
        """
        initialises an instance of Square

        Args:
        size (int, optional): the size of the square. Defaults is 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
