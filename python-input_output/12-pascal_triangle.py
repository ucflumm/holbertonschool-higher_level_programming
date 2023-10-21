#!/usr/bin/python3
""" Module: 12-pascal_triangle.py """


def pascal_triangle(n):
    """
        returns a list of lists of integers representing the Pascal’s
        triangle of n
    """
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        row = [1]
        prev = pascal[i - 1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        pascal.append(row)
    return pascal
