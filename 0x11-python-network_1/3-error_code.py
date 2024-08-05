#!/usr/bin/python3
'''eoor handling'''

from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen, Request


if __name__ == "__main__":
    try:
        with urlopen(Request(argv[1])) as res:
            content = res.read()
            print(content.decode('utf-8'))
    except HTTPError as exception:
        print('Error code:', exception.code)
