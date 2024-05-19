#!/usr/bin/python3
"""
    A module that contains the function from_json_string
"""
import json


def from_json_string(my_str):
    """
        A function that returns an object
        Python data structure represented by a JSON
        string

        Args:
            my_str: The JSON string

        Returns:
            The python object
    """
    return json.loads(my_str)
