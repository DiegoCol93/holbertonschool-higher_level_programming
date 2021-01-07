#!/usr/bin/python3
""" Module: MagicClass bytecode dissasembly challenge. """
import math


class MagicClass:
    """ Class: MagicClass Bytecode reconstruction."""

    def __init__(self, radius):
        """"Method for initialize a circle object
            with validation of the data type of radius variable.

        Args:
            radius(int): Radius of the circle.

        Return:
            Always nothing.

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """Method to calculate the area of the circle.

        Args:
            Any argument.

        Return:
            Area of the circle.

        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """"Method to calculate the circumference of the circle.

        Args:
            Any argument.

        Return:
            Circumference of the circle.

        """
        return ((2 * math.pi) * self.__radius)
