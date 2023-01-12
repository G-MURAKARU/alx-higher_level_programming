#!/usr/bin/python3

"""
    Defines a class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):  # sourcery skip: raise-specific-error
        """
        area finds area

        Raises:
            Exception: area not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> None:
        # sourcery skip: use-fstring-for-formatting
        """
        integer_validator validates an input integer

        Args:
            name (str): quantity represented by value
            value (int): input integer
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle defines the class Rectangle

    Args:
        BaseGeometry (class): parent class
    """

    def __init__(self, width: int, height: int) -> None:
        super().__init__()
        super().integer_validator(name="width", value="width")
        self.__width = width
        super().integer_validator(name="height", value=height)
        self.__height = height
