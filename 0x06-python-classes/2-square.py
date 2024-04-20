#!/usr/bin/python3
'''shebang'''


class Square:
    '''Square class'''

    def __init__(self, size=0):
        '''initilizing size to 0 '''

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
