#!/usr/bin/python3
""" Makes a POST request with the email and url passed as arguments. """

if __name__ == "__main__":

    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv as av

    d = {"email": av[2]}
    data = urlencode(d)
    data = data.encode('utf-8')

    request = Request(av[1], data)
    with urlopen(request) as response:
        print(response.read().decode("utf-8"))
