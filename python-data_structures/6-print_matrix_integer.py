#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):                   # each matrix row
            print("{:d}".format(row[i]), end="")
            if i < len(row) - 1:                    # if not last element
                print(" ", end="")                  # add space
        print()
