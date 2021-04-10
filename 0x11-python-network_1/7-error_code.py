#!/usr/bin/python3
""" Prints the content of a page, or the response's error code. """
from requests import get
from sys import argv as av
if __name__ == "__main__":

    # Gets url, av[1] = "URL".
    response = get(av[1])

    # Gets status code.
    status = response.status_code

    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
