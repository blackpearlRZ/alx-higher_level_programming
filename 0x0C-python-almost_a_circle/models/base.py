#!/usr/bin/python3
'''
This module provides the Base class which serves as the base for all other classes in this project.

The Base class manages the id attribute to ensure unique identification of each instance.
'''
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

