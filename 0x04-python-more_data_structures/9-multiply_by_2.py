#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _new = {}
    for i, _value in a_dictionary.items():
        _new[i] = _value * 2
    return _new
