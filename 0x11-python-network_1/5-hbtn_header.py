#!/usr/bin/python3
""" Gets the content of https://intranet.hbtn.io/status using requests. """
from requests import get
print(get('https://intranet.hbtn.io/status').headers["X-Request-Id"])
