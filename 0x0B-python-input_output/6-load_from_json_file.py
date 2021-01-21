#!/usr/bin/python3
""" Module for storing the load_from_json_file function. """
import json


def load_from_json_file(filename):
    """ Loads an object from a JSON format stored in a file. """
    with open(filename) as json_txt:
        return json.loads(json_txt.read())
