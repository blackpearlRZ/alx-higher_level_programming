#!/usr/bin/python3
'''shebangu'''
from models.base import Base


class Rectangle(Base):
    '''Represent a rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initilizing height,width,x,y n id'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

     @property
    def width(self):
        '''set n  get rec width'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''set n get rectangle height'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("heigt must be an integer")
        if value <= 0:
            raise ValueError("height must >= 0")
        self.__height = value

    @property
    def x(self):
        '''set n get x coordinates'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''set n get y coordinates'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
