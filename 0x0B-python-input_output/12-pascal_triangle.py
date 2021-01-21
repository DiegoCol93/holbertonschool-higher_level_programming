#!/usr/bin/python
""" Module for printing the pascal value up to 5. """


def pascal_triangle(n):
    """ Function to calculate and create the list.

        Args:
            n Number for pascal's triangle.

        Returns:
            the_list(list), created according to the input number n.
    """
    the_list = []

    if n > 0:

        for row in range(n):

            the_inner_list = []
            for column in range(row + 1):

                if column == 0 or column == row:
                    the_inner_list.append(1)

                else:
                    the_inner_list.append(the_list[row - 1][column - 1] +
                                          the_list[row - 1][column])

            the_list.append(the_inner_list)

    return(the_list)
