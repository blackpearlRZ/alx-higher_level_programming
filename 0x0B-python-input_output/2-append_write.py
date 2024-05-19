#!/usr/bin/python3
"""
    A module that contains the function append_write
"""


def append_write(filename="", text=""):
    """
        A function that appends a string at the end
        of a text file

        Args:
            filename (str): The file
            text: The string to append

        Returns:
            number: The number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        number = f.write(text)
    return number
