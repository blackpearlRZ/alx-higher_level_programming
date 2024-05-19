#!/usr/bin/python3
"""
    A module that contains the function to_json_string
"""
import json


def to_json_string(my_obj):
    """
        A function that returns the JSON representation
        of an object(string)

        Args:
            my_obj: The object

        Returns:
            The JSON representation
    """
    return json.dumps(my_obj)
