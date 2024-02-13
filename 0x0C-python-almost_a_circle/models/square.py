#!/usr/bin/python3
"Square Module"
from models.rectangle import Rectangle


class Square(Rectangle):
    "Square Class"
    def __init__(self, size, x=0, y=0, id=None):
        "Initialization method"
        if id is None:
            id = 1
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        "Getter for size"
        return self.width

    @size.setter
    def size(self, value):
        "Setter for size"
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        "Update attributes based on arguments and/or keywords"
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        "Return a string representation of the Square instance"
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        "Return the dictionary representation of the Square"
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
