#!/usr/bin/python3
'''err '''

from sys import argv
import requests


if __name__ == "__main__":
    uRl = "http://0.0.0.0:5000/search_user"
    holder = ""
    if len(argv) > 1:
        holder = {"q": argv[1][0]}
    r = requests.post(uRl, data=holder)
    try:
        response = r.json()
        if response:
            f_respose = "[{}] {}"
            print(f_respose.format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
