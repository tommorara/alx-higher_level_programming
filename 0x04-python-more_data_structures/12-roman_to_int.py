#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    _roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
    }
    _result = 0
    _former = 0
    for q in roman_string[::-1]:
        _value = _roman_values[q]
        if _value >= _former:
            _result += _value
        else:
            _result -= _value
        _former = _value
    return _result
