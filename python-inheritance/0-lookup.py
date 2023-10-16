#!/usr/bin/python3
"""
    Module 0-lookup
    Write a function that returns the list of available attributes
    and methods of an object:
"""


def lookup(obj):
    """
        lookup method to look up attributes and methods
        of an object
    """
    attributes_and_methods = dir(obj)

    return attributes_and_methods
