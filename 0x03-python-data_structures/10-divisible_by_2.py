#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    verify_list = []
    for i in my_list:
        if i % 2 == 0:
            verify_list.append(True)
        else:
            verify_list.append(False)
    return verify_list
