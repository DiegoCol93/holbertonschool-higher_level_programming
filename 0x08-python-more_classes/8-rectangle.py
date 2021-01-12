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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ __init__:

            Args:
                width (int): Of the Rectangle instance.
                height (int): Of the Rectangle instance.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    # __str__ method. # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __str__(self):
        """ Printing method via __str__. """

        rect_string = ''

        if self.height > 0 and self.width > 0:

            colums = 0
            while colums < self.height:

                rows = 0
                while rows < self.width:

                    rect_string += '#'
                    rows += 1

                rect_string += '\n'
                colums += 1

            return(rect_string[0: -1])
        else:
            return(rect_string)

    # __repr__ method. # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __repr__(self):
        """ Representation of the object in a string format """
        r_repr = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return r_repr

    # __del__ method # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __del__(self):
        """ __del__ method for deleting a Rectangle instance. """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # bigger_or_equal static method # # # # # # # # # # # # # # # # # # # # # #
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ bigger_or_equal method:

            Args:
                rect_1 (Rectangle): Instance of the Rectangle class.
                rect_2 (Rectangle): Instance of the Rectangle class.

            Returns:
                rect_1 if it is larger or equal in area as rect_2 or
                rect_2 otherwise.

            Raises:
                TypeError: if rect_1 or rect_2 are not Rectangle class objects.
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
