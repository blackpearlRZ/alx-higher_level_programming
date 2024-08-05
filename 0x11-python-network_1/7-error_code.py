#!/usr/bin/python3
'''err '''

from sys import argv
import requests


if __name__ == '__main__':
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
