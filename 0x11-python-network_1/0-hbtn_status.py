#!/usr/bin/python3
'''url status'''

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        res = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print(f"\t- content: {res}")
        print("\t- utf8 content: {}".format(res.decode("utf-8")))
