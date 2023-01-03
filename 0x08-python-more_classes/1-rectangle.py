#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """
    This is a class that defines a rectangle
    """

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """
        __init__ initialises a new Rectangle object

        Args:
            width (int, optional): rectangle's width. Defaults to 0.
            height (int, optional): rectangle's height. Defaults to 0.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        width retrieves the rectangle's width

        Returns:
            int: rectangle's width
        """

        return self.__width

    @width.setter
    def width(self, value: int):
        """
        width _summary_

        Args:
            value (int): the desired rectangle's width

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        height retrieves the rectangle's height

        Returns:
            int: rectangle's height
        """

        return self.__height

    @height.setter
    def height(self, value: int):
        """
        height _summary_

        Args:
            value (int): the desired rectangle's height

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
