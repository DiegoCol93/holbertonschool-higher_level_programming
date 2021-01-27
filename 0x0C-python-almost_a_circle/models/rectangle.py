#!/usr/bin/python3
""" Module for storing Rectangle class. """
from models.base import Base  # <-- import Base class
from collections import OrderedDict


class Rectangle(Base):
    """ Rectangle model class, inherits from Base form model class. """
    # __init__ | Private | method |-------------------------------------------|
    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__:

            Args:
                width(int): Value for the width of the Rectangle.
                height(int): Value for the height of he Rectangle.
                x(int): Value for the offset for display's x position.
                y(int): Value for the offset for display's y position.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # __str__ | Private | method |--------------------------------------------|
    def __str__(self):
        """ Returns the string for the Rectangle object """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    # Validate int | Public | method |----------------------------------------|
    def validate_int(self, name, number):
        """ Validates if the given number is an integer. """
        if type(number) is not int:
            raise TypeError("{} must be an integer".format(name))

    # area | Public | method |------------------------------------------------|
    def area(self):
        """ Returns the area of the Rectangle object. """
        return self.width * self.height

    # display | Public | method |---------------------------------------------|
    def display(self):
        """ Prints the Rectangle object using width and height. """
        print("\n" * self.y, end='')
        for i in range(self.height):
            for j in range(self.width + self.x):
                if j < self.x:
                    print(' ', end='')
                else:
                    print('#', end='')
            print('')

    # update | Public | method |----------------------------------------------|
    def update(self, *args, **kwargs):
        """ Updates all attributes of the Rectangle object. """

        if bool(args) is True and args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for i in kwargs.keys():
                if i in dir(self):
                    setattr(self, i, kwargs[i])

    # to_dictionary | Public | method |---------------------------------------|
    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle object. """
        ret_dict = OrderedDict()
        ret_dict["id"] = self.id
        ret_dict["width"] = self.width
        ret_dict["height"] = self.height
        ret_dict["x"] = self.x
        ret_dict["y"] = self.y
        return dict(ret_dict)

    # Set & Get __width | Public | method |------------------------------------
    @property
    def width(self):
        """ Getter of the Rectangle's width value. """
        return self.__width

    @width.setter
    def width(self, number):
        """ Setter of the Rectangle's width value. """
        self.validate_int("width", number)
        if number <= 0:
            raise ValueError("width must be > 0")
        self.__width = number

    # Set & Get __height | Public | method |-----------------------------------
    @property
    def height(self):
        """ Getter of the Rectangle's height value. """
        return self.__height

    @height.setter
    def height(self, number):
        """ Setter of the Rectangle's height value. """
        self.validate_int("height", number)
        if number <= 0:
            raise ValueError("height must be > 0")
        self.__height = number

    # Set & Get __x | Public | method |----------------------------------------
    @property
    def x(self):
        """ Getter of the Rectangle's x value. """
        return self.__x

    @x.setter
    def x(self, number):
        """ Setter of the Rectangle's x value. """
        self.validate_int("x", number)
        if number < 0:
            raise ValueError("x must be >= 0")
        self.__x = number

    # Set & Get __y | Public | method |----------------------------------------
    @property
    def y(self):
        """ Getter of the Rectangle's y value. """
        return self.__y

    @y.setter
    def y(self, number):
        """ Setter of the Rectangle's y value. """
        self.validate_int("y", number)
        if number < 0:
            raise ValueError("y must be >= 0")
        self.__y = number
