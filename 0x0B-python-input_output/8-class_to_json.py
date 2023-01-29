#!/usr/bin/python3

"""
    this is the ``8-class_to_json`` module.
    this module provides one function, class_to_json(obj: Any)
"""


def class_to_json(obj) -> dict:
    """
    class_to_json returns dictionary description with simple data structures
    for JSON serialization of a input object [obj]

    Args:
        obj (Any): input obj - an instance of a class

    Returns:
        dict: dict representation of JSON
    """

    return obj.__dict__
