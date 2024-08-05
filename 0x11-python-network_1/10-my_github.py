#!/usr/bin/python3
'''github '''

from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(r.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
