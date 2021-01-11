#!/usr/bin/python3
"""|    | Module: For storing the Rectangle Class. |   |
|                                                   |
|      _____   __  ______  ______  ______           |
|     /\  __-./\ \/\  ___\/\  ___\/\  __ \          |
|     \ \ \/\ \ \ \ \  __\  \ \__ \ \ \/\ \         |
|      \ \____-\ \_\ \_____\ \_____\ \_____\        |
|       \/____/ \/_/\/_____/\/_____/\/_____/        |
|      __      ______  ______  ______  ______       |
|     /\ \    /\  __ \/\  == \/\  ___\/\___  \      |
|     \ \ \___\ \ \/\ \ \  _-/\ \  __\ /_/  /__     |
|      \ \_____\ \_____\ \_\   \ \_____\/\_____\    |
|       \/_____/\/_____/\/_/    \/_____/\/_____/    |
|                                                   |
|                   | Jan-2021 |                    |
"""


class Rectangle:
    """ Rectangle class object with height and width. """
    def __init__(self, width=0, height=0):
        """ __init__:

            Args:
                width (int): Of the Rectangle instance.
                height (int): Of the Rectangle instance.
        """
        self.width = width
        self.height = height

    # __height getter and setter # # # # # # # # # # # # # # # # # # # # # # #
    @property
    def height(self):
        """ height get method: gets the private __height value. """
        return self.__height

    @height.setter
    def height(self, value):
        """ height set method: Setter

        Arg:
            value (int): Value for the height of the Rectangle object.

        Raises:
            TypeError:  height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is int:
            if value >= 0:
                self.__height = value  #: Set private __height value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    # __width getter and setter # # # # # # # # # # # # # # # # # # # # # # # #
    @property
    def width(self):
        """ width get method: gets the private __height value. """
        return self.__width

    @width.setter
    def width(self, value):
        """ width set method: Setter.

        Arg:
            value (int): Value for the width of the Rectangle object.

        Raises:
            TypeError:  width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is int:
            if value >= 0:
                self.__width = value  #: Set private __width value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    # area getter. # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def area(self):
        """ area method:

        Returns: the area of the Rectangle, height * width.
        """
        return (self.height * self.width)

    # perimeter getter. # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def perimeter(self):
        """ perimeter method:

        Returns: the perimeter of the Rectangle, 2 * height * 2 * width.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (2 * self.height + 2 * self.width)
