#!/usr/bin/python3
"""
    Module: save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
        writes an Object to a text file, using a JSON representation
    """
    # Open the file name mode write and encoding utf-8 and dump the object
    with open(filename, mode='w', encoding='utf-8') as f:
        # Dump the object args my_obj to the file f
        json.dump(my_obj, f)
