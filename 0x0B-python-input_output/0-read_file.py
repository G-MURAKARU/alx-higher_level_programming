#!/usr/bin/python3


def read_file(filename="") -> None:
    """
    read_file reads an input .txt file

    Args:
        filename (str, optional): file to be read. Defaults to "".
    """

    with open(file=filename, mode="r") as my_file:
        print(my_file.read())
