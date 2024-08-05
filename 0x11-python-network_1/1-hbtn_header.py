#!/usr/bin/python3
'''yadi yadi yada'''


import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        print(dict(response.headers).get("X-Request-Id"))
