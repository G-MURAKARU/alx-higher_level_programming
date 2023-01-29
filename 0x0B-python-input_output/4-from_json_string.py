#!/usr/bin/python3

"""
    this is the ``4-from_json_string`` module.
    this module provides one function, from_json_string(my_str: str).
"""

import json
from typing import Any


def from_json_string(my_str: str) -> Any:
    """
    from_json_string deserializes input [my_str] JSON string

    Args:
        my_str (str): JSON string to deserialize

    Returns:
        Any: deserializes python object
    """

    return json.loads(my_str)
