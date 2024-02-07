#!/usr/bin/python3
"""class Student that defines a
student by: (based on 9-student.py)
"""


class Student:
    "class Student that defines a student"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        filtered_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_attrs[attr] = getattr(self, attr)
        return filtered_attrs

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
