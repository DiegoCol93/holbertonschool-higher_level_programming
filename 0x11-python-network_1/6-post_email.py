#!/usr/bin/python3
""" Posts an email to the given url. """
from requests import post
from sys import argv as av

# av[1] = "URL", av[2] = "email"

print(post(av[1], data={'email': av[2]}).text)
