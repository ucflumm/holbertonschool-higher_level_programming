#!/usr/bin/python3
"""
    My list Module: my_list
"""


class MyList(list):
    """
        Class Mylist extends from list
    """
    def print_sorted(self):
        """
            Prints sorted list
            args:
                self: the list

            Return: None
        """
        print(sorted(self))
