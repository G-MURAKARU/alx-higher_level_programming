#!/usr/bin/python3

"""
    this is the ``0-read_file`` module.
    this module provides one function, read_file(filename: str)
"""


def read_file(filename: str = "") -> None:
    """
    read_file reads an input .txt file

    Args:
        filename (str, optional): file to be read. Defaults to "".
    """

    with open(file=filename, mode="r", encoding="UTF-8") as my_file:
        print(my_file.read())
