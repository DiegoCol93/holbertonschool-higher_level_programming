#!/usr/bin/python3
""" Module: for printing figures """


def print_square(size):
    """ Function: For printing a square

        Args:
            size (int): Size of square

        Raises:
            TypeError: if not an int
            ValueError: Size less than 0
    """

    if (type(size) is float and size < 0) or type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        print("#" * size)
