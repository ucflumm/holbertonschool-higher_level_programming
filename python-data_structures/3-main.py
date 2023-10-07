#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

# Empty test 1
a = []
print_reversed_list_integer(a)

# Empty test 2
print_reversed_list_integer([])
# Expected Output: (no output)
# Explanation: When an empty list is provided, there should be no output.
