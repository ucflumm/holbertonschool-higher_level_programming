#!/usr/bin/python3
"""defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    # Check that all rows have the same size
    first_row_size = len(matrix[0])
    if not all(len(row) == first_row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(all(isinstance(element, (int, float)) for element in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    return [[round(element / div, 2) for element in row] for row in matrix]
