#!/usr/bin/python3
"""
    A module that contains the add_integer function
"""


def add_integer(a, b=98):
    """
    A function that adds two integers

    Args:
        a: first integer
        b: second integer

    Return:
        The sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    a = int(a)
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    b = int(b)
    return a + b
