#!/usr/bin/python3
"""
    A module that contains the print_square function
"""


def print_square(size):
    """
        A function that prints a square

        Args:
            size (int): The size of the squre

        Raises:
            TypeError: if the size is not an integer or < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for dot in range(size):
        for dotdot in range(size):
            print("#", end="")
        print("")
