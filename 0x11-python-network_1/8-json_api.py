#!/usr/bin/python3
''' Sends a POST to query the /search_user api. '''
from sys import argv as av
from requests import post
if __name__ == '__main__':

    if len(av) > 1 and bool(av[1]):
        value = av[1]
    else:
        value = ''

    payload = {'q': value}
    response = post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        response.json
        json = eval(response.text)
        if bool(json):
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
