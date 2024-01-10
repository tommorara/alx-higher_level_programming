#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _new_matrix = [[0 for _ in range(len(row))] for row in matrix]
    for q in range(len(matrix)):
        for r in range(len(matrix[q])):
            _new_matrix[q][r] = matrix[q][r] ** 2
    return _new_matrix
