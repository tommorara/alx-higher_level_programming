#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        int_max = my_list[0]
        for q in range(len(my_list)):
            if my_list[q] > int_max:
                int_max = my_list[q]
        return int_max
