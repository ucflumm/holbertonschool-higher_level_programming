#!/usr/bin/python3
"""
    10-student.py
"""


class Student:
    """
        Class student that defines a student by: (based on 9-student.py)
        - first_name
        - last_name
        - age
    """
    def __init__(self, first_name, last_name, age):
        """
            Parameterized Constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            if attrs is a list of strings, only attribute names contained
            in this list must be retrieved. Otherwise, all attributes must be
            retrieved.
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict
