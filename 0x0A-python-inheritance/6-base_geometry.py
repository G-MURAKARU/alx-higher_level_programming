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
