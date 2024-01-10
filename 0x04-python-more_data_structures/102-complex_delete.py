#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _keys_to_delete = [_key for _key, _val in
                       a_dictionary.items() if _val == value]
    for _key in _keys_to_delete:
        del a_dictionary[_key]
    return a_dictionary
