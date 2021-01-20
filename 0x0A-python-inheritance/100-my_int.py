#!/usr/bin/python3
""" Module for storing MyInt clss. """


class MyInt(int):
    """ My integer inherits from integer """

    def __eq__(self, other):
        """ equal to """
        return False if (int(self) is other) else True

    def __ne__(self, other):
        """ different than """
        return True if (int(self) is other) else False
