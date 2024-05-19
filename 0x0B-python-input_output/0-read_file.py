#!/usr/bin/python3
"""
    A module that contains the function read_file
"""


def read_file(filename=""):
    """
        A function that reads a text file and prints it to stdout

        Args:
            filename (str): The text file to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.readlines()
    for line in text:
        print(line, end="")
