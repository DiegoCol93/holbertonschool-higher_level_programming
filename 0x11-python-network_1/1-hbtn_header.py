#!/usr/bin/python3
""" Requests the value of a response header "X-Request-Id". """

if __name__ == "__main__":

    from urllib.request import urlopen
    from sys import argv as av

    with urlopen(av[1]) as response:
        headers = response.info()
        header = "X-Request-Id"
        print(headers.get(header))
