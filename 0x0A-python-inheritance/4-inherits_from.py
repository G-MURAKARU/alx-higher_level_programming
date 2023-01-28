#!/usr/bin/python3

"""
    this is the ``4-inherits_from`` module.
    this module provides one function, inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class) -> bool:
    """
    inherits_from checks if the input object obj's class is a subclass of
    the input class a_class

    Args:
        obj (any): input object
        a_class (_type_): input class

    Returns:
        bool: True if it is a subclass; otherwise False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
