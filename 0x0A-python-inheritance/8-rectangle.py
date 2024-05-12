#!/usr/bin/python3
'''shbang'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle presentation'''
    def __init__(self, width, height):
        '''rectangle init initilization'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
