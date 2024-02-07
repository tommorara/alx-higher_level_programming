#!/usr/bin/python3
"""function that returns the dictionary description
with simple data structure (list, dictionary,
string, integer and boolean) for
JSON serialization of an object
"""


def class_to_json(obj):
    "returns the dictionary description with simple data structure"
    serializable_attributes = {}
    for attribute, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            serializable_attributes[attribute] = value

    return serializable_attributes
