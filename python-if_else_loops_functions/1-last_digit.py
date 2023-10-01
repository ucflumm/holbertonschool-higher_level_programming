#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    numberLastDigit = number % 10
    number = number * -1
else:
    numberLastDigit = number % 10
if numberLastDigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, numberLastDigit))
elif numberLastDigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, numberLastDigit))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, numberLastDigit))