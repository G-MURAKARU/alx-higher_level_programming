#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    try:
        my_list.remove(my_list[idx])
        return my_list
    except IndexError:
        return my_list
