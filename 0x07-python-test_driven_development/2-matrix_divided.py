#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ Function that divides value in a matrix by specified value"""
    result_matrix = []
    for row in matrix:
        new_row = []
        for val in row:
            new_row.append(round((val/3), 2))
        result_matrix.append(new_row)

    return (result_matrix)
