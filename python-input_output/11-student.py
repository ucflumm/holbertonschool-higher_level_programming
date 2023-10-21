#!/usr/bin/python3
"""
    Module: 11-student.py
    """


class Student:
    """
        Class student that defines a student by: (based on 10-student.py)
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

    def reload_from_json(self, json):
        """
            replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __repr__(self):
        """
            Return:
                string representation of the object
        """
        return "[Student] {} - {} - {}".format(self.first_name,
                                               self.last_name, self.age)

    def __str__(self):
        """
            Return:
                string representation of the object
        """
        return "[Student] {} - {} - {}".format(self.first_name,
                                               self.last_name, self.age)
