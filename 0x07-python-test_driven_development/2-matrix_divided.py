#!/usr/bin/python3
""" Module: 2-matrix_divided """


def matrix_divided(matrix, div):
    """ matrix_divided: Divides a matrix over a number.

        Args:
            matrix (list): Input list of lists.
            div (int, float): Divisor to dived over.

        Return:
            The new divided matrix.

        Raises:
            TypeError: when not correct type used.
            ZeroDivisionError: when dividing by zero.
    """

    # Error messages
    mtrxType_err = 'matrix must be a matrix (list of lists) of integers/floats'
    mtrxSize_err = 'Each row of the matrix must have the same size'
    div_Type_err = 'div must be a number'
    div_Zero_err = 'division by zero'
    # Init of the new matrix.
    div_mtrx = []

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(mtrxType_err)

    if type(div) not in (int, float):
        raise TypeError(div_Type_err)

    if div == 0:
        raise ZeroDivisionError(div_Zero_err)

    for row in matrix:
        div_row = []

        if type(row) is not list or len(row) == 0:
            raise TypeError(mtrxType_err)

        elif len(row) != len(matrix[0]):
            raise TypeError(mtrxSize_err)

        for item in row:
            if type(item) not in (int, float):
                raise TypeError(mtrxType_err)
            div_row.append(round((item / div), 2))

        div_mtrx.append(div_row)

    return(div_mtrx)
