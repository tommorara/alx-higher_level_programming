#!/usr/bin/python3
"""function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """You must use the with statement
    You don’t need to manage file permission
    or file doesn't exist exceptions.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
