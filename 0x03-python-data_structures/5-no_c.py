#!/usr/bin/python3
def no_c(my_string):
    recent = ""
    for i in my_string:
        if i not in "cC":
            recent += i
    return recent
