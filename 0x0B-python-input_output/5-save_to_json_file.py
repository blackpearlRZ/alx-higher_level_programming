#!/usr/bin/python3
"""
    A module that contains the function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
        A function that write an Object to a text file
        using a JSON representation

        Args:
            my_obj: The Object to write
            filename: The file to write in
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
