#!/usr/bin/python3
'''post email'''


from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    if len(argv) > 2:
        data = parse.urlencode({'email': argv[2]}).encode('ascii')
        r = request.Request(argv[1], data)
        with request.urlopen(r) as res:
            html = res.read()
            print(html.decode('utf-8'))
