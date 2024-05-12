#!/usr/bin/python3
'''shbang'''


class BaseGeometry:
    '''geo class'''
    def area(self):
        '''error handlin'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''rectangle presentation'''
    def __init__(self, width, height):
        '''rectangle init initilization'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''ssadi2ni  law ba3raf a2olak'''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
