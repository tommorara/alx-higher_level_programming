#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list.copy()
    recent = list(my_list)
    recent[idx] = element
    return recent
