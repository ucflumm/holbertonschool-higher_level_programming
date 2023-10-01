#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberLastDigit = number % 10
if numberLastDigit < 0:
    print(f'Last digit of {number} is {numberLastDigit} and is less than 6 and not 0')
elif number == 0:
    print(f'Last digit of {number} is {numberLastDigit} and is 0')
elif number > 0:
    print(f'Last digit of {number} is {numberLastDigit} and is greater than 5')
