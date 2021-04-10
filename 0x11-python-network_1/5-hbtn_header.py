#!/usr/bin/python3
""" Gets the response of a specific header https://intranet.hbtn.io/status """
from requests import get
print(get('https://intranet.hbtn.io/status').headers["X-Request-Id"])
