#!/usr/bin/python3
"This is a Module for a Rectangle class."

from models.base import Base


class Rectangle(Base):
    "Class representing a rectangle"
    def __init__(self, width, height, x=0, y=0, id=None):
        "Initialize a Rectangle instance"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        "Get width of the rectangle"
        return self.__width

    @width.setter
    def width(self, value):
        "Set the width of the rectangle"
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "Get the height of the rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        "Set the height of the rectangle"
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        "Get the x-coordinate of the rectangle."
        return self.__x

    @x.setter
    def x(self, value):
        "Set the x-coordinate of the rectangle."
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        "Get the y-coordinate of the rectangle."
        return self.__y

    @y.setter
    def y(self, value):
        "Set the y-coordinate of the rectangle."
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        "calculate and return the area of the rectangle"
        return self.__width * self.__height

    def display(self):
        """Display the rectangle with '#' characters
        Taking care of x and y
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """update attributes with no_keyword arguments
        and key-worded arguments
        """
        attr_list = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(min(len(args), len(attr_list))):
                setattr(self, attr_list[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        "Return the string representation of the Rectangle instance"
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self):
        "Return the dictionary representation of the Rectangle"
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
