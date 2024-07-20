#!/usr/bin/python3
'''
This module provides the Base class which serves as the base for all
other classes in this project.

The Base class manages the id attribute to ensure unique
identification of each instance.
'''
import json


class Base:
    '''The base class for all other classes
        It's purpose is to manage ID attribute
        '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Class constructor

            Args:
                id (int, optional): The id of the object
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return the JSON serialization of dicts's listsu'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
