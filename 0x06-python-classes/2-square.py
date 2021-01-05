#!/usr/bin/python3
''' Module: For defining the Square class. '''


class Square:
    ''' Class: For defining a Square object. '''
    def __init__(self, size=0):
        ''''Args:
    size (int): Size of the square.'''
        if isinstance(size, (int)) is True:      # Is size a digit ?
            if size < 0:                                # Is size less than 0 ?
                raise ValueError("size must be >= 0")
            else:
                self.__size = size                      #: init attribute.
        else:
            raise TypeError("size must be an integer")
