#!/usr/bin/python3

"""
    this is the ``1-write_file`` module.
    this module provides onr function, write_file(filename: str, text: str)
"""


def write_file(filename="", text="") -> int:
    """
    write_file writes the input [text] to the given input [filename]
    if [filename] does not exist, it creates the file and writes to it
    if [filename] exists, it overwrites its contents with [text]

    Args:
        filename (str, optional): file to (over)write to. Defaults to "".
        text (str, optional): text to (over)write. Defaults to "".

    Returns:
        int: number of written characters
    """

    with open(file=filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
