#!/usr/bin/python
""" Module for printing the pascal value up to 5. """


def pascal_triangle(n):
    """ Function to calculate and create the list.

        Args:
            n Number for pascal's triangle.

        Returns:
            the_list(list), created according to the input number n.
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
