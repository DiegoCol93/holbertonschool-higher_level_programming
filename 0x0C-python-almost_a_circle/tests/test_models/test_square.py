#!/usr/bin/python3
""" Test module for storing Square class test cases. """
import unittest
from models.base import Base
from models.square import Square
from unittest.mock import patch
from io import StringIO
from time import sleep


print_on = 0
class TestSquare(unittest.TestCase):
    """ TestSquare class for storing the unittest methods and cases. """
    if print_on == 1:
        green = "\033[92m"  # <-- Stores the green text color format.
        reset = "\033[0m"  # <-- Stores the reset text color format.
        print(green + "." + "~ " * 11 + "| test_square.py module. |" +
              "~ " * 11 + reset)
        sleep(1)

    # Tests from 9-main.py ---------------------------------------------------|
    def test_9_Square(self):
        """ Test cases for Square class objects, from 9-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 9-main.py " + "~" * 19 +
                  reset)

        s1 = Square(5)
        # Test print(s1)
        case_string = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .area() == 25
        self.assertEqual(s1.area(), 25)

        # Test .display()
        case_string = "#####\n" * 5
        with patch('sys.stdout', new = StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        s2 = Square(2, 2)
        # Test print(s2)
        case_string = "[Square] (2) 2/0 - 2\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s2)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .area() == 4
        self.assertEqual(s2.area(), 4)

        # Test .display()
        case_string = "  ##\n" * 2
        with patch('sys.stdout', new = StringIO()) as fake_out:
            s2.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        s3 = Square(3, 1, 3)
        # Test print(s3)
        case_string = "[Square] (3) 1/3 - 3\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s3)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .area() == 9
        self.assertEqual(s3.area(), 9)

        # Test .display()
        case_string = "\n" * 3 + " ###\n" * 3
        with patch('sys.stdout', new = StringIO()) as fake_out:
            s3.display()
            self.assertEqual(fake_out.getvalue(), case_string)

    # Tests from 10-main.py --------------------------------------------------|
    def test_10_Square(self):
        """ Test cases for Square class objects, from 10-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 10-main.py " + "~" * 18 +
                  reset)

        s1 = Square(5)
        # Test print(s1)
        case_string = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .size()
        self.assertEqual(s1.size, 5)

        s1.size = 10
        case_string = "[Square] (1) 0/0 - 10\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test pass a "string" to size.
        with self.assertRaises(TypeError):
            s1.size = "9"

    # Tests from 11-main.py --------------------------------------------------|
    def test_11_Square(self):
        """ Test cases for Square class objects, from 11-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 11-main.py " + "~" * 18 +
                  reset)

        # Test Create a Square
        s1 = Square(5)
        case_string = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(10)
        s1.update(10)
        case_string = "[Square] (10) 0/0 - 5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(1, 2)
        s1.update(1, 2)
        case_string = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(1, 2, 3)
        s1.update(1, 2, 3)
        case_string = "[Square] (1) 3/0 - 2\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(1, 2, 3, 4)
        s1.update(1, 2, 3, 4)
        case_string = "[Square] (1) 3/4 - 2\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(x=12)
        s1.update(x=12)
        case_string = "[Square] (1) 12/4 - 2\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(size=7, y=1)
        s1.update(size=7, y=1)
        case_string = "[Square] (1) 12/1 - 7\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(size=7, id=89, y=1)
        s1.update(size=7, id=89, y=1)
        case_string = "[Square] (89) 12/1 - 7\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test from 13-main.py - update(**kwargs) ---------------------------------|
    def test_13_Squares(self):
        """ Test cases for Square class objects, from 13-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 13-main.py " +
                  "~" * 19 + reset)

        s1 = Square(10, 2, 1)
        case_string = "[Square] (1) 2/1 - 10\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Return Dictionary
        s1_dictionary = s1.to_dictionary()
        case_dict = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        # Test if the dictionary is the correct one.
        self.assertEqual(s1_dictionary, case_dict)
        # Test the type of the return.
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        case_string = "[Square] (2) 1/0 - 1\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s2)
            self.assertEqual(fake_out.getvalue(), case_string)

        s2.update(**s1_dictionary)
        case_string = "[Square] (1) 2/1 - 10\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s2)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test that r1 is different tha r2
        self.assertFalse(s1 == s2)

    # Test for update() method.
    def test_Square_update(self):
        """ Test cases for the .display() """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 19 + " Testing Square.update() method. " +
                  "~" * 17 + reset)

        # Case when both *args and **kwargs are used.
        s = Square(1)
        s.update(2, id=100)
        case_string = "[Square] (2) 0/0 - 1\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s)
            self.assertEqual(fake_out.getvalue(), case_string)

    def tearDown(self):
        """ Resets the Base class counter after each test unit. """
        Base._Base__nb_objects = 0

if __name__ == '__main__':
    unittest.main()
