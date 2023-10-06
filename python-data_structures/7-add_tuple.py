#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure that both tuples have at least 2 elements by
    # padding with zeros if needed
    while len(tuple_a) < 2:
        tuple_a += (0,)
    while len(tuple_b) < 2:
        tuple_b += (0,)

    # Perform element-wise addition and return the result as a tuple
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result_tuple
