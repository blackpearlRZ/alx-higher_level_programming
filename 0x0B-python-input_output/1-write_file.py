#!/usr/bin/python3
"""
    A module that contains the functin write_file
"""


def write_file(filename="", text=""):
    """
        A function that writes a string to a text file

        Args:
            filename (str): The file name
            text (str): The string to write

        Returns:
            The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        number = f.write(text)
        return number
