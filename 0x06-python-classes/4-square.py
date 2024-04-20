#!/usr/bin/python3
'''shbang'''


class Square:
    '''init class square'''

    def __init__(self, size=0):
        '''initilizing size 0'''
        self.size = size

    @property
    def size(self):
        '''set /get suare size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' find/return area of the square.'''
        return (self.__size * self.__size)
