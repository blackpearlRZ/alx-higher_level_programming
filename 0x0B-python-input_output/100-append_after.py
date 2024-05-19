#!/usr/bin/python3
"""
    A module that contains the function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
        A function that inserts a line of text to a file
        after each line cntaining a specific string

        Args:
            filename (str): The name of the file
            search_string (str): The string to look for
            new_string (str): The line to append
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            if search_string in line:
                f.write(line + new_string)
            else:
                f.write(line)
