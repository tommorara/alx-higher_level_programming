#!/usr/bin/python3

"class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"


class Rectangle:
    """
    Private instance attribute: width:
    property def width(self): to retrieve it
    property setter def width(self, value): to set it:
    width must be an integer, otherwise raise a
    TypeError exception with the message width must be an integer
    if width is less than 0, raise a ValueError
    exception with the message width must be >= 0
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width
                         for _ in range(self.__height)])

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__width}, {self.__height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
