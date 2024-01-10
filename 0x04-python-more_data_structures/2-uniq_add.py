#!/usr/bin/python3
def uniq_add(my_list=[]):
    _uniq_int = set()
    for q in my_list:
        _uniq_int.add(q)
    _result = sum(_uniq_int)
    return _result
