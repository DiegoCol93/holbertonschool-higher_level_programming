#!/usr/bin/python3
''' Prints my Github userid using the Github's API '''
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv as av
if __name__ == "__main__":

    r = get('https://api.github.com/user', auth=HTTPBasicAuth(av[1], av[2]))
    try:
        info = r.json()
        print(info['id'])
    except ValueError:
        print('None')
