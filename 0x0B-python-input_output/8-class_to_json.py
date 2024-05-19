#!/usr/bin/python3
"""
    A module that contains the function class_to_json
"""


def class_to_json(obj):
    """
        A function that returns the dictionary description
        with simple data structure(list, dict, str, int, bool)
        for JSON serialization of an object

        Args:
            obj: The object

        Returns:
            The dict representation
    """
    return vars(obj)
