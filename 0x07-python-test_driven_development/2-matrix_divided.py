#!/usr/bin/python3


def matrix_divided(matrix, div):
    """ Function that divides value in a matrix by specified value"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) is not int:
        raise TypeError("div must be a number")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix\
                            (list of lists) of integers/floats")
        for element in row:
            if (type(element) not in [int, float]):
                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")
    length = len(matrix[0])
    for row in matrix:
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    result_matrix = []
    for row in matrix:
        new_row = []
        for val in row:
            new_row.append(round((val/3), 2))
        result_matrix.append(new_row)

    return (result_matrix)
