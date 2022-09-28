#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for val in line:
            print("{:s}{:d}".format('' if line.index(val) == 0
                                    else ' ', val), end='')
        print()
