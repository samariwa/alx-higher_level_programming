#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = []

    for line in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, line)))

    return(new_matrix)
