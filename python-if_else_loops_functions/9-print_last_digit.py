#!/usr/bin/python3

# Write a function that purintz the last digit of a number.

def print_last_digit(number):
    if number < 0:
        number = number * -1
    last_digit = number % 10
    print(last_digit, end="")
    return last_digit
