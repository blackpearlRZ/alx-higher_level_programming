#!/usr/bin/python3

class Base:
    '''creating base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        ''''initilizing id'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

