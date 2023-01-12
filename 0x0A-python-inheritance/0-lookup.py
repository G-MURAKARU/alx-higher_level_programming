#!/usr/bin/python3


def lookup(obj):
    """
    lookup returns a list of the available attributes and methods of an object

    Args:
        obj (Any): the object to investigate

    Returns:
        list: list of attributes and methods
    """

    return list(dir(obj))
