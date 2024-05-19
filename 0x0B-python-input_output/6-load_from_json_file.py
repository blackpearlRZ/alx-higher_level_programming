#!/usr/bin/python3
"""
    A module that contains the function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
        A function that creates an Object from a JSON file

        Args:
            filename: The JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        obj = json.load(f)
    return obj
