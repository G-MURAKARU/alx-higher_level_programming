#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    try:
        list_str = list(str)
        list_str.remove(list_str[n])
        return ''.join(list_str)
    except IndexError:
        return str
