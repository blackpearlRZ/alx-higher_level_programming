#!/usr/bin/python3
''' sends a request to URL and displays the value X-Request-Id'''

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
