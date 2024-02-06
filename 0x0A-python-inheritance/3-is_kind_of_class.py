#!/usr/bin/python3
"""function that returns True if the object
is an instance of, or if the object is an instance
of a class that inherited 4rm, the
specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class
    that inherited 4rm, the specified class
    """
    return isinstance(obj, a_class)
