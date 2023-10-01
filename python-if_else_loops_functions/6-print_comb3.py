#!/usr/bin/python3

# Write a program that prints all possible
# different combinations of two digits.


for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            print("{:d}{:d}".format(i, j), end="")
            if i < 8:
                print(", ", end="")
print("")
