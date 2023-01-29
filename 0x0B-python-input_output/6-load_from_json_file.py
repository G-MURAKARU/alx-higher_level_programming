#!/usr/bin/python3

"""
    this is the ``6-load_from_json_file`` module.
    this module provides one function, load_from_json_file(filename: str)
"""

import json
from typing import Any


def load_from_json_file(filename: str) -> Any:
    """
    load_from_json_file deserializes JSON to a python object

    Args:
        filename (str): json file to load

    Returns:
        Any: Python object from JSON
    """

    with open(file=filename, mode="r") as my_file:
        return json.load(my_file)
