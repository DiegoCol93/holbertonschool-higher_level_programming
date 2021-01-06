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
        if self.__position[1] > 0:
            lines = "\n" * self.__position[1]
            print(lines, end='')
        if self.__size > 0:
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
        error = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(error)
        else:
            for i in value:
                if type(i) is not int or i < 0:
                    raise TypeError(error)
                else:
                    continue
        self.__position = value
