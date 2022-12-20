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
            size (int, optional): the square's sides' length. Defaults to 0.

        Raises:
            TypeError: raised when the passed size argument is not an integer
            ValueError: raised when the passed size argument is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size: int = size

    @property
    def size(self):
        """
        size is a getter for the private size instance attribute

        Returns:
            size (int): length of sides
        """
        return self.__size

    @size.setter
    def size(self, custom_size: int):
        """
        size is a setter for the private size instance attribute

        Args:
            custom_size (int): size to assign to size instance attribute
        """
        self.__size = custom_size

    def area(self):
        """
        area finds the area of a square instance
        """
        return self.__size**2
