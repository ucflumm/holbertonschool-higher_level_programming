#!/usr/bin/python3

# Write a program that prints all numbers from 0 to 98
# in decimal and in hexadecimal (as in the following example)
# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store numbers or strings in a variable
# You are not allowed to import any module

for i in range(0, 99):
    print("{:d} = 0x{:x}".format(i, i))
