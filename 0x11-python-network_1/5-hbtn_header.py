#!/usr/bin/python3
''' sends a request to URL and displays the value X-Request-Id'''

from sys import argv
import requests


if __name__ == '__main__':
    print(requests.get(argv[1]).headers.get('x-Request-Id'))
