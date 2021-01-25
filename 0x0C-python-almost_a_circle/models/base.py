#!/usr/bin/python3
""" Module for storing the Base class. """
import json
import csv
from collections import OrderedDict


class Base():
    """ Class: Base, stores the basic attributes of the Base objects. """

    __nb_objects = 0  # <-- Class level variable, counts number of objects.

    # __init__ | Private | method |-------------------------------------------|
    def __init__(self, id=None):
        """ __init__:

            Args:
                id(int): value for the id of the new instance of the class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # draw | Public | Static-method |----------------------------------------||
    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw: Prints the objects on an external Xwindow.

        Args:
            list_rectangles(list): List of Rectangle class objects.
            list_squares(list): List of Square class objects.
                                  ___
                               ,+'/.\'+,    ___
                              \/\_/\_/\_/\,+' * \
                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            /_/'-------'\_\
        """
        # Setup for the screen.
        import turtle
        from random import randint
        screen = turtle.getscreen()
        screen.title("Almost A Circle!!")
        screen.setup(width=500, height=500, startx=None, starty=None)
        turtle.setworldcoordinates(-40, -7, 180, 180)
        turtle.hideturtle()
        turtle.speed(1)
        screen.bgcolor("black")
        screen.colormode(255)
        turtle.pensize(3)

        # method for actually drawing stuff.--------------------------------|||
        def move_turtle(list_r, list_s):
            """
            Moves the turtle according to the object's dimensions and
             the offset given by obj.x and obj.y and draws, it using
             a different random color each time.

            Args:
                list_rectangles(list): List of Rectangle class objects.
                list_squares(list): List of Square class objects.
            """
            for obj in list_r:
                # Sets the turtle's pen for next Rectangle obj on the list.
                turtle.pu()
                turtle.home()
                turtle.setpos(obj.x, obj.y)
                turtle.pencolor(randint(80, 255),
                                randint(80, 255),
                                randint(80, 255))
                for lines in range(2):
                    # Starts drawing the Rectangle obj.
                    turtle.pd()
                    turtle.forward(obj.width)
                    turtle.left(90)
                    turtle.forward(obj.height)
                    turtle.left(90)

            for obj in list_s:
                # Sets the turtle's pen for next Square obj on the list.
                turtle.pu()
                turtle.home()
                turtle.setpos(obj.x, obj.y)
                turtle.pencolor(randint(80, 255),
                                randint(80, 255),
                                randint(80, 255))
                for lines in range(4):
                    # Starts drawing the Square obj.
                    turtle.pd()
                    turtle.forward(obj.size)
                    turtle.left(90)

        # Draws the title, the circle and the credits.
        def draw_title():
            turtle.pu()
            turtle.setpos(71, 155)
            turtle.pencolor(randint(80, 255),
                            randint(80, 255),
                            randint(80, 255))
            turtle.write("              Almost a Circle\n" +
                         "By Diego Lopez @HolbertonSchool\n" +
                         "                      2021",
                         False, align="center", font=("Arial", 16, "normal"))
            turtle.pu()

        draw_title()
        move_turtle(list_rectangles, list_squares)
        turtle.getscreen()._root.mainloop()  # <---Keeps window open.

    # save_to_file_csv | Public | Class-method |-----------------------------||
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)
        list_of_dictionaries = list(map(cls.to_dictionary, list_objs))
        for dictionary in list_of_dictionaries:
            list_of_headers = list(dictionary.keys())

        with open(filename, 'w', newline='') as scv_file:
            writer = csv.DictWriter(scv_file, list_of_headers)
            writer.writeheader()
            writer.writerows(list_of_dictionaries)

    # load_from_file_csv | Public | Class-method |---------------------------||
    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        list_of_dictionaries = []
        tmp_dictionary = {}
        list_of_objects = []
        try:
            with open(filename, newline='') as scv_file:
                reader = csv.DictReader(scv_file)
                for row in reader:
                    for key in row:
                        tmp_dictionary[key] = int(row[key])
                    dummy = cls.create(**tmp_dictionary)
                    list_of_objects.append(dummy)

        except FileNotFoundError:
            list_of_objects = []

        return(list_of_objects)

    # save_to_file | Public | Class-method |----------------------------------|
    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file:

            Args:
                list_objs(list): List of class type objects(Rectangle, Square)
        """
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is None:
            pass
        else:
            list_dict = list(map(cls.to_dictionary, list_objs))

        with open(filename, "w") as json_txt_file:
            json_txt_file.write(cls.to_json_string(list_dict))

    # load_from_file | Public | Class-method |--------------------------------|
    @classmethod
    def load_from_file(cls):
        """ load_from_file:

            Returns:
                List of objects of the type of the <class> calling this method
                loads from the file by the name of <class>.json
                If file does not exist returns an empty list.
        """
        filename = "{}.json".format(cls.__name__)
        list_of_dictionaries = []
        list_of_objects = []

        try:
            with open(filename) as json_txt:
                list_of_dictionaries = cls.from_json_string(json_txt.read())
                for attributes in list_of_dictionaries:
                    list_of_objects.append(cls.create(**attributes))

        except FileNotFoundError:
            list_of_objects = []

        return list_of_objects

    # to_json_string | Public | Static-method |-------------------------------|
    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string:

            Args:
                list_dictionaries(list): List of dictionaries to format.

            Returns:
                the JSON format string of the object.
        """
        return json.dumps(list_dictionaries)

    # from_json_string | Public | Static-method |-----------------------------|
    @staticmethod
    def from_json_string(json_string):
        """ from_json_string:

            Args:
                json_string(str): JSON string to return as list of dictionaries

            Returns:
                list of dictionaries, empty list if json_string is None.
        """
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    # create | Public | Class-method |----------------------------------------|
    @classmethod
    def create(cls, **dictionary):
        """ Returns an object with pre-set attributes.

            Args:
                dictionary(dict): 'key':For setting the pre-set attributes.

            Return:
                An instance of the class.
        """
        default = cls(1, 1)
        default.update(**dictionary)
        return(default)
