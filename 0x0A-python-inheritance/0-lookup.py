#!/usr/bin/python3
"""
    this is the ``0-lookup`` module
    this module provides one function, lookup(obj)
"""


def lookup(obj) -> list[str]:
    """
    lookup returns a list of the available attributes and methods of an object

    Args:
        obj (Any): the object to investigate

    Returns:
        list: list of attributes and methods
    """

    return list(dir(obj))
