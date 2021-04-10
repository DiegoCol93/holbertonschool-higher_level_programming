#!/usr/bin/python3
""" Gets the response of a specific header at the given url. """
from requests import get
from sys import argv
print(get(argv[1]).headers["X-Request-Id"])
