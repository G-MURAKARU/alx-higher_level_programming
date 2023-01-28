#!/usr/bin/python3

"""
    this is the ``10-square`` module
    this module defines one class, Square,
    that inherits from another class, Rectangle.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square defines a Square object

    Args:
        Rectangle (BaseGeometry): parent/base class
    """

    def __init__(self, size: int) -> None:
        """
        __init__ is the square object constructor

        Args:
            size (int): square's sides' length
        """

        super().integer_validator("size", size)
        self.__size: int = size

    def area(self) -> int:
        """
        area finds the mathematical area of the square

        Returns:
            int: square's area
        """

        return self.__size**2
