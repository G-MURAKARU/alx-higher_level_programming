#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    lt = len(my_list)
    if lt > 0:
        for x in range(lt - 1, -1, -1):
            print("{:d}".format(my_list[x]))
    else:
        print()
    return
