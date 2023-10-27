#!/usr/bin/python3
"""
    Module square containing the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class extends Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return a string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the square """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
