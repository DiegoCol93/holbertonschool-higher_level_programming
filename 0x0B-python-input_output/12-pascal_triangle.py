#!/usr/bin/python3
"""Module pascal's triangle"""


def pascal_triangle(n):
    """ Function that returns a list of list of pascal triangle.
    Args:
        n: Pascal number.
    Return:
        list of lists of integers representing the
        Pascals triangle of n.
    """
    p_list = []
    if n <= 0:
        return p_list
    if n == 1:
        return [[1]]
    p_list = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(p_list[i - 1][j - 1] + p_list[i - 1][j])
        row.append(1)
        p_list.append(row)
    return p_list
