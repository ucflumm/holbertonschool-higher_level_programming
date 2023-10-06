#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

# Test case 1: Basic test with a list of integers
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

# Check if the result is an error message
if isinstance(list_result, str):
    print(list_result)
else:
    # Print the results using a loop
    for i in range(len(list_result)):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))

# Test case 2: List with a single element
my_list = [42]
list_result = divisible_by_2(my_list)

# Check if the result is an error message
if isinstance(list_result, str):
    print(list_result)
else:
    # Print the results using a loop
    for i in range(len(list_result)):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))

# Test case 3: Empty list
my_list = []
list_result = divisible_by_2(my_list)

# Check if the result is an error message
if isinstance(list_result, str):
    print(list_result)
else:
    # Print the results using a loop
    for i in range(len(list_result)):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))

# Test case 4: List with zero (handled by error message)
my_list = [1, 2, 0, 4, 5]
list_result = divisible_by_2(my_list)

# Check if the result is an error message
if isinstance(list_result, str):
    print(list_result)
else:
    # Print the results using a loop
    for i in range(len(list_result)):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))

# Test case 5: List with mixed types (handled by error message)
my_list = [1, 2, '3', 4, 5]
list_result = divisible_by_2(my_list)

# Check if the result is an error message
if isinstance(list_result, str):
    print(list_result)
else:
    # Print the results using a loop
    for i in range(len(list_result)):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
