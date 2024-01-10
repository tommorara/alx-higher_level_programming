#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    _sum_values = sum(_score * _weight for _score, _weight in my_list)
    _sum_weights = sum(_weight for _, _weight in my_list)
    if _sum_weights == 0:
        return 0
    return _sum_values / _sum_weights
