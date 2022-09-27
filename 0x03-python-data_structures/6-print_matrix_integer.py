#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for val in line:
            print ("{:d}".format(val), end='')
        print()
