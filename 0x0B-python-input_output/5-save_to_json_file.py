#!/usr/bin/python3

"""
    this is the ``5-save_to_json_file`` module.
    this module provides one function,
    save_to_json_file(my_obj: Any, filename: str)
"""

import json
from typing import Any


def save_to_json_file(my_obj: Any, filename: str) -> None:
    """
    save_to_json_file writes a JSON-serialized [my_obj] to a
    text file [filename]

    Args:
        my_obj (Any): object to serialize to JSON
        filename (str): file to write JSON representation of [my_obj]
    """

    with open(file=filename, mode="w") as my_file:
        my_file.write(json.dumps(my_obj))
