#!/usr/bin/python3
"""a function that adds 2 integers
a and b must be integers or floats, otherwise
raise a TypeError exception with the message
a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):

    """a function that adds 2 integers
    Returns an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    result = a + b
    return (result)
