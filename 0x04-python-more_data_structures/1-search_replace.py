#!/usr/bin/python3
def search_replace(my_list, search, replace):
    _new_list = [replace if q == search else q for q in my_list]
    return _new_list
