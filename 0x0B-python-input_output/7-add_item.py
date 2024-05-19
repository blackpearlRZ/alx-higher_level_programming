#!/usr/bin/python3
"""
    A script that adds all arguments to a Python List
    and then save them to a file
"""

import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    py_list = []
    if os.path.exists('add_item.json'):
        py_list = load_from_json_file('add_item.json')
    for arg in argv[1:len(argv)]:
        py_list.append(arg)
    save_to_json_file(py_list, 'add_item.json')
