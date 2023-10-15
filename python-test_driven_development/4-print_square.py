#!/usr/bin/python3
"""module 4-print_square.py"""


def print_square(size):
    """function that prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
