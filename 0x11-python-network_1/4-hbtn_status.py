#!/usr/bin/python3
""" Gets the content of https://intranet.hbtn.io/status using requests. """
from requests import get
response = get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
