#!/usr/bin/python3
"""This module contains the BaseModel class"""


class Base:
    """
        Base class for all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return the JSON string representation of list_dictionaries
        """
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
            Return the list of the JSON string representation json_string
        """
        import json
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
