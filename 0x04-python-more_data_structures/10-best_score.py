#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    max_value = max(values)
    max_value_index = values.index(max_value)
    max_key = keys[max_value_index]
    return max_key
