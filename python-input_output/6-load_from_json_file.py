#!/usr/bin/python3
"""
    Module: load_from_json_file
    """
import json


def load_from_json_file(filename):
    """
        creates an Object from a “JSON file”
    """
    # Open the file name mode read and encoding utf-8 and load the object
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
