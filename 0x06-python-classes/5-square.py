#!/usr/bin/python3
'''shebangu'''


class Square:
    '''init class sqaure'''

    def __init__(self, size):
        '''init size'''
        self.size = size

    @property
    def size(self):
        '''set- get square size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''returns square area'''
        return (self.__size * self.__size)

    def my_print(self):
        '''priniting da square'''
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
