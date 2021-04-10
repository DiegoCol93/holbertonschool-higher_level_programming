#!/usr/bin/python3
""" Gets the response of a specific header at the given url. """
from requests import get
from sys import argv as av
if __name__ == "__main__":
    print(get(av[1]).headers["X-Request-Id"])
