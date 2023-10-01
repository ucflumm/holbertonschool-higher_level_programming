#!/usr/bin/python3

# Write a program that prints the number of and the list of its arguments.

import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc - 1))
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))
