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

    def integer_validator(self, name, value) -> None:
        # sourcery skip: use-fstring-for-formatting
        """
        integer_validator validates an input integer

        Args:
            name (str): quantity represented by value
            value (int): input integer
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
