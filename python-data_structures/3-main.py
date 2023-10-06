#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
a = []
print_reversed_list_integer(a)

print_reversed_list_integer([])
# Expected Output: (no output)
# Explanation: When an empty list is provided, there should be no output.

#print_reversed_list_integer([1, 2, 3, 4, 5])
# Expected Output:
# 5
# 4
# 3
# 2
# 1
# Explanation: The function should print the integers in reverse order.

#print_reversed_list_integer([-1, -2, -3, -4, -5])
# Expected Output:
# -5
# -4
# -3
# -2
# -1
# Explanation: The function should correctly handle negative integers.

#print_reversed_list_integer([1, -2, 3, -4, 5])
# Expected Output:
# 5
# -4
# 3
# -2
# 1
# Explanation: The function should correctly handle a mix of positive and negative integers.

#print_reversed_list_integer([0])
# Expected Output:
# 0
# Explanation: The function should correctly handle a list with a single integer (zero in this case).

#print_reversed_list_integer([1, 1, 2, 2, 3, 3])
# Expected Output:
# 3
# 3
# 2
# 2
# 1
# 1
# Explanation: The function should handle duplicate integers correctly.

#print_reversed_list_integer([1000000, 999999, 100000, 99999])
# Expected Output:
# 99999
# 100000
# 999999
# 1000000
# Explanation: The function should work with large integers as well.
3