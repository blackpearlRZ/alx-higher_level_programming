#!/usr/bin/python3

"""
This module provides the Rectangle class which
serves as a subclass of Base.

The Rectangle class manages attributes related
to rectangle dimensions and coordinates.
"""

from models.base import Base


class Rectangle(Base):
    '''Rectangle class inheriting from Base.
    Manages width, height, x, and y attributes.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X coordinate of the rectangle.
            y (int): Y coordinate of the rectangle.
            id (int, optional): ID of the rectangle.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Gets the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width of the rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is <= 0.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Gets the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is <= 0.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Gets the x coordinate of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Sets the x coordinate of the rectangle.

        Args:
            value (int): New x value.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is < 0.
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Gets the y coordinate of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Sets the y coordinate of the rectangle.

        Args:
            value (int): New y value.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is < 0.
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''returns rectangl earea'''
        return self.width * self.height

    def display(self):
        '''prints the Rectangle using the #'''
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        '''update tasku'''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        '''returns the rectangle dict representation'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''Return the string representation of the rectangle.'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
