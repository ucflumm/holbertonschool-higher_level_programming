#!/usr/bin/python3
"""Module 5-text_indentation.py"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these
    characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in range(len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print(text[i])
                print()
            else:
                print(text[i], end="")
