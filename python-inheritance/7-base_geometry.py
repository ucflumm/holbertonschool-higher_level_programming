#!/usr/bin/python3
"""
    Module: BaseGeometry
"""


class BaseGeometry:
    """
        Class BaseGeometry
    """
    def area(self):
        """
            Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates value
            args:
                name: name of the value
                value: value to validate

            Raises:
                TypeError: if value is not an integer
                ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
