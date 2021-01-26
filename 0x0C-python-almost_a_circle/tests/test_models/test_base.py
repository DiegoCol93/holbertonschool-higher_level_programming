#!/usr/bin/python3
""" Test module for storing Base class test cases. """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
from time import sleep


print_on = 0 # <-- Set to 1 to activate printing of the tests.
class TestBase(unittest.TestCase):
    """ TestBase class for storing the unittest methods and cases. """
    if print_on == 1:
        green = "\033[92m"  # <-- Stores the green text color format.
        reset = "\033[0m"  # <-- Stores the reset text color format.
        print(green + "." + "~ " * 11 + "~| test_base.py module. | " +
              "~ " * 11 + reset)
        sleep(1)

    # Tests from 0-main.py----------------------------------------------------|
    def test_0_Base(self):
        """ Tests the cases for the Base class from 0-main.py """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + '.' + "~" * 20 + " Testing cases from 0-main.py " +
                  "~" * 19 + reset)
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    # Tests from 14-main.py----------------------------------------------------|
    def test_14_Base(self):
        """ Tests the cases for the Base class from 14-main.py """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + '.' + "~" * 20 + " Testing cases from 14-main.py " +
                  "~" * 19 + reset)

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string(sorted(dictionary.items()))
        case = '[["height", 7], ["id", 1], ["width", 10], ["x", 2], ["y", 8]]'
        self.assertEqual(json_string, case)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_string), str)

        # Testing None case.
        empty = Base.to_json_string(None)
        self.assertEqual(empty, "[]")

        # Testing empty case.
        empty = Base.to_json_string([])
        self.assertEqual(empty, "[]")


    def test_15_Base(self):
        """ Tests the cases for the Base class from 15-main.py """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + '.' + "~" * 20 + " Testing cases from 15-main.py " +
                  "~" * 19 + reset)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        sum_save = 0
        case = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, ' +
                '{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')

        sum_expected = sum(list(map(lambda letter: ord(letter), case)))

        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new = StringIO()) as fake_out:
                sum_save = sum(list(map(lambda letter: ord(letter),
                                        file.read())))
            self.assertEqual(sum_save, sum_expected)

        r3 = Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_15_Base(self):
        """ Tests the cases for the Base class from 15-main.py """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + '.' + "~" * 20 + " Testing cases from 15-main.py " +
                  "~" * 19 + reset)




    # Tests for the Base class instance. -------------------------------------|
    def test_instance(self):
        """ Test cases for the Base class instance and it's types """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertTrue(type(b1) == Base)

    # Teardown method for resetting the count of instances in Base class.-----|
    def tearDown(self):
        """ Resets the Base class counter after each test unit. """
        Base._Base__nb_objects = 0

if __name__ == '__main__':
    unittest.main()
