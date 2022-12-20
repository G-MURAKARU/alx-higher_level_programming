#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    This is a class that defines a square
    """

    def __init__(self, size: int) -> None:
        """
        __init__ Initialises a new Square instance

        Args:
            size (integer): the length of the sides of the square
        """
        self.__size: int = size
