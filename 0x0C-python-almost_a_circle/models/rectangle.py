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
