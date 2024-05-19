#!/usr/bin/python3
"""10-student"""


class Student:
    """ A class that defines a student """
    def __init__(self, first_name, last_name, age):
        """ an instance of Student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of a Student """

        if type(attrs) is list and all(type(x) is str for x in attrs):
            return {attr: getattr(self, attr) for
                    attr in attrs if hasattr(self, attr)}
        return self.__dict__
