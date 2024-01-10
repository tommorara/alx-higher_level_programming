#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _sorted = sorted(a_dictionary.keys())
    for q in _sorted:
        print("{}: {}".format(q, a_dictionary[q]))
