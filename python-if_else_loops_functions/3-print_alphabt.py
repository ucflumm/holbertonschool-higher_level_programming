#!/usr/bin/python3
# Write a program that prints the ASCII alphabet,
# in lowercase, not followed by a new line.

for i in range(97, 123):
    if i != 113 and i != 101:
        print(chr(i), end='')
