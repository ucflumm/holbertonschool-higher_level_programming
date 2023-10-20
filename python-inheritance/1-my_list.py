#!/usr/bin/python3
"""My list module my_list"""


class MyList(list):
    """Class Mylist"""
    def print_sorted(self):
        "Prints list sorted"
        print(sorted(self))
