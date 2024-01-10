#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        _max = max(a_dictionary.values())
        _best = [q for q, _value in a_dictionary.items() if _value == _max][0]
        return _best
    return None
