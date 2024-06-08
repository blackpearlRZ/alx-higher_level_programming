#!/usr/bin/python3
"""
    A module that contain the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
        A function that says my name

        Args:
            first_name (str): The first name
            last_name (str, optional): The last name

        Raises:
            TypeError: If first_name or last_name aren't a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
