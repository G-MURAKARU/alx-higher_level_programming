#!/usr/bin/python3

"""
    this is the ``7-add_item`` module.
    this module provides one function, add_item(...)
"""


def add_items(filename: str) -> None:
    """
    add_items adds CLI arguments to a list and saves them to a JSON file

    Args:
        filename (str): json file to save args to
    """

    load_from_json_file = __import__(
        "6-load_from_json_file"
    ).load_from_json_file
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

    try:
        input_cache: list = load_from_json_file(filename)
    except FileNotFoundError:
        input_cache = []
    finally:
        input_cache.extend(sys.argv[1:])
        save_to_json_file(input_cache, filename)


if __name__ == "__main__":
    import sys

    file = "add_item.json"
    add_items(filename=file)
