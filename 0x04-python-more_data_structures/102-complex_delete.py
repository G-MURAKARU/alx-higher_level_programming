#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values = list(a_dictionary.values())
    ind = -1
    not_found = False
    indices = []

    while not not_found:
        try:
            ind = values.index(value, ind + 1)
        except ValueError:
            not_found = True
        else:
            indices.append(ind)
    if ind == -1:
        return a_dictionary

    keys = list(a_dictionary.keys())
    for ind in indices:
        del a_dictionary[keys[ind]]

    return a_dictionary
