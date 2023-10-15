#!/usr/bin/python3
"""Module for 5-text_indentation.py"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these
    characters: ., ?, and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_line = True  # A flag to indicate whether a new line is needed

    for char in text:
        if char in ('.', '?', ':'):
            print(char, end='\n\n')
            new_line = True
        elif new_line and char == ' ':
            continue  # Skip leading space
        else:
            if new_line:
                print(char, end='')
                new_line = False
            else:
                print(char, end='')
