#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    new_matrix = matrix.copy()
    while i < len(matrix):
        new_matrix[i] = list(map(lambda x: x * x, matrix[i]))
        i += 1
    return(new_matrix)
