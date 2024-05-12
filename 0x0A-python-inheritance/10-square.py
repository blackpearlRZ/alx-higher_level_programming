#!/usr/bin/python3
'''shbang'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class that inherits from rec'''
    def __init__(self, size):
        '''init for square'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''modifyin area return'''
        return self.__size ** 2
