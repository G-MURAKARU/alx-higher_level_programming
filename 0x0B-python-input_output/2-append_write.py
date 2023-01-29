#!/usr/bin/python3

"""
    this is the ``2-append_write`` module
    this module provides one function, append_write(filename: str, text: str)
"""


def append_write(filename: str = "", text: str = "") -> None:
    """
    append_write appends the input [text] to the input [filename]

    Args:
        filename (str, optional): name of file to edit. Defaults to "".
        text (str, optional): text to append to [filename]. Defaults to "".
    """
    with open(file=filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
