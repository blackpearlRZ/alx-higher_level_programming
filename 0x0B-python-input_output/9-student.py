#!/usr/bin/python3
"""
    A module that contains the class Student
"""


class Student():
    """
        A class that defines a Student by:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        An attribute constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A method that retrives a dictionary repr of a Student
        """
        return vars(self)
