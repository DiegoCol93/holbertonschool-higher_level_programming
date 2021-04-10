#!/usr/bin/python3
""" Posts an email to the given url. """
from requests import post
from sys import argv as av

if __name__ == "__main__":
    # av[1] = "URL", av[2] = "email"
    payload = { "email": av[2] }
    print(post(av[1], data=payload))
