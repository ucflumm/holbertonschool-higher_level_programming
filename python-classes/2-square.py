#!/usr/bin/python3
"""Definition of class Square"""


class Square:
    """Class square with attribute size"""

    def __init__(self, size=0):
        """ Initialize the square with a given size """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2

    @property
    def size(self):
        """ Return the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def my_print(self):
        """ Print the square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
