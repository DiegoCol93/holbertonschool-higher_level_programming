#!/usr/bin/python3
""" Module: For defining the Square class. """


class Square:
    """ Class: For defining a Square object. """
    def __init__(self, size=0, position=(0, 0)):
        """__init__:

        Args:
            size (int): Size of the square.
            position (tuple): Position for printing.
        """
        self.size = size
        self.position = position

    def area(self):
        """ area: Returns the area of the Square instance. """
        return (self.__size * self.__size)

    def my_print(self):
        """ my_print: Prints Square instance using '#'. """
        if self.__size > 0:
            if self.__position[1] > 0:
                lines = "\n" * self.__position[1]
                print(lines, end='')
            for lines in range(0, self.__size):
                for columns in range(0, self.__size + self.__position[0]):
                    if columns >= self.__position[0]:
                        print("#", end='')
                    else:
                        print(" ", end='')
                print()
        else:
            print()

    @property
    def size(self):
        """ size: Gets the size of the Square instance. """
        return self.__size

    @size.setter
    def size(self, value):
        """ size: Sets the size of the square instance with value. """
        if isinstance(value, (int)) is True:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value  #: Set size value.
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ position: Gets the value of position. """
        return self.__position

    @position.setter
    def position(self, value):
        """ position: Sets the position for printing.

        Args:
            value (tuple): Position for printing.
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """ Method: For printing the Square instance directly. """
        square_string = ""
        if self.__size > 0:
            square_string += "\n" * self.__position[1]
            for i in range(0, self.__size):
                square_string += (" " * self.__position[0] + "#" * self.__size
                                  + "\n")
        return square_string[0: -1]
