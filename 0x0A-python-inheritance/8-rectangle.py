#!/usr/bin/python3

"""
    this is the ``8-rectangle`` module.
    this module defines one class Rectangle.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle defines the rectangle object

    Args:
        BaseGeometry (...): parent class
    """

    def __init__(self, width: int, height: int) -> None:
        """
        __init__ is the rectangle object constructor

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        print(type(height))

        self.__width = width
        self.__height = height
