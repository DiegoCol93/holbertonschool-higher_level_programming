#!/usr/bin/python3
""" Module: 0-add_integer """


def add_integer(a, b=98):
    """ add_integer: Adds two numbers a + b

        By default b is set to 98 and only receives
        type int or float numbers, casts to int the
        given float numbers before adding.

        Args:
            a (int) or (float): First number to add.
            b (int) or (float): First number to add.

        Returns:
            Result: of a + b operated as ints.

        Raises:
            TypeError: If the incorrect type was used.
    """
    if type(a) in (int, float):
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) in (int, float):
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
