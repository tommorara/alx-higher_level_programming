#!/usr/bin/python3

"""
function that prints a text with 2 new lines 
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    text must be a string, otherwise raise
    a TypeError exception with the message text must be a string
    There should be no space at the beginning
    or at the end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punc = [".", "?", ":"]
    i = 0
    while i < len(text) and text[i] == " ":
        i = i + 1
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in punc:
            if text[i] in punc:
                print("\n")
            i = i + 1
            while i < len(text) and text[i] == " ":
                i = i + 1
            continue
        i = i + 1
