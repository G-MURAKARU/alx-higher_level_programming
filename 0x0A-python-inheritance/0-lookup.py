#!/usr/bin/python3
"""
    function lookup
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
