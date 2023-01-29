#!/usr/bin/python3

"""
    this is the ``3-to_json_string`` module.
    this module provides one function, to_json_string(my_obj: Any)
"""

import json
from typing import Any


def to_json_string(my_obj: Any) -> str:
    """
    to_json_string serializes input [my_obj] to JSON

    Args:
        my_obj (Any): object to serialize

    Returns:
        str: JSON string representation of [my_obj]
    """

    return json.dumps(my_obj)
