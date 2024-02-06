#!/usr/bin/python3
"empty class BaseGeometry"


class BaseGeometry:
    "empty class BaseGeometry"
    def area(self):
        "no implementation for method yet"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "validates value"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from
    BaseGeometry (7-base_geometry.py)
    """
    def __init__(self, width, height):
        "initialize the rectangle"
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        "returns area of the rectangle"
        return (self.__width * self.__height)

    def __str__(self):
        "return the rectangle description"
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
