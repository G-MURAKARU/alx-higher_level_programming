#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    
    num, denom = 0, 0
    for score, weight in my_list:
        num += score * weight
        denom += weight

    return num/denom
