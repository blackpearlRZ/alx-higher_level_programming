#!/usr/bin/python3
'''shebang'''


class Square:
    '''initilizing class'''

    def __init__(self, size=0):
        '''Initializing size to 0'''
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        '''Return the current area of the square.'''
        return (self.__size * self.__size)
