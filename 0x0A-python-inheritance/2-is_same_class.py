#!/usr/bin/python3

"""
    this is the ``2-is_same_class`` module.
    this module provides one function, is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class) -> bool:
    """
    is_same_class checks if obj is exactly an instance of a_class

    Args:
        obj (any): object to investigate
        a_class (any): possible object class

    Returns:
        bool: whether obj is an instance of a_class or not
    """

    return type(obj) == a_class
