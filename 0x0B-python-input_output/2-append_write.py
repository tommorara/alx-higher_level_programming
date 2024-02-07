#!/usr/bin/python3
"""function that appends a string at the end of a
text file (UTF8) and returns the
number of characters added
"""


def append_write(filename="", text=""):
    """If the file doesn’t exist, it should be created
    You must use the with statement
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
