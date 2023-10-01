#!/usr/bin/python3

# Write a program that imports the function CENSORED from the file
# CENSORED and prints the result of the addition 1 + 2 = 3

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
