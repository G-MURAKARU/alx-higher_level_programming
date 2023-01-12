#!/usr/bin/python3


def write_file(filename="", text="") -> int:
    with open(file=filename, mode="w") as my_file:
        return my_file.write(text)
