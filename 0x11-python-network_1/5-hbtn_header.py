#!/usr/bin/python3
""" Gets the response of a specific header https://intranet.hbtn.io/status. """
from requests import get
from sys import argv as av
if __name__ == "__main__":
    print(get(av[1]).headers["X-Request-Id"])
