#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    This is a class that defines a square
    """

    def __init__(self, size: int = 0) -> None:
        """
        __init__ Initialises a new Square instance

        Args:
            size (int, optional): the length of the sides of the square. Defaults to 0.

        Raises:
            TypeError: raised when the passed size argument is not an integer
            ValueError: raised when the passed size argument is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size: int = size
