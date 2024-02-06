#!/usr/bin/python3
"class MyInt that inherits from int"


class MyInt(int):
    "class MyInt that inherits from int"
    def __init__(self, value):
        "initialize the class MyInt"
        self.value = value

    def __equal__(self, other):
        "MyInt has == and != operators inverted"
        return self.value != other

    def __notequal__(self, other):
        "MyInt has == and != operators inverted"
        return self.value == other
