#!/usr/bin/python3
""" Module for storing MyInt clss. """


class MyInt(int):
    """ My integer inherits from integer """

    def __eq__(self, other):
        """ not equal to """
        return int(self) != other

    def __ne__(self, other):
        """ equal to """
        return int(self) == other
