#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Test case 1: Basic test with a list of integers
my_list = [1, 3, 5, 2, 4]
print(max_integer(my_list))  # Expected output: 5

# Test case 2: List with negative numbers
my_list = [-1, -3, -5, -2, -4]
print(max_integer(my_list))  # Expected output: -1

# Test case 3: List with a single element
my_list = [42]
print(max_integer(my_list))  # Expected output: 42

# Test case 4: Empty list
my_list = []
print(max_integer(my_list))  # Expected output: None

# Test case 5: List with duplicate maximum values
my_list = [7, 3, 7, 2, 7]
print(max_integer(my_list))  # Expected output: 7

# Test case 6: List with mixed types (should raise an error)
my_list = [1, 2, '3', 4, 5]
# This will raise a TypeError since the list contains a non-integer element
# Uncomment the line below to test it
print(max_integer(my_list))