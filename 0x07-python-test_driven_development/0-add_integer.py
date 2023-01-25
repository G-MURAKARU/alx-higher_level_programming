#!/usr/bin/python3
"""
    this is the ``0-add_integer`` module
    the add_integer module supplies one function, add_integer().
"""


def add_integer(a: int, b: int = 98) -> int:
    """
    add_integer computes arithmetic addition between two integers a and b

    Args:
        a (int): first integer to add
        b (int, optional): second integer to add. Defaults to 98.

    Returns:
        int: sum of integers a and b
    """

    def validate(num: tuple) -> int:
        """
        validate validates that the input values are integers or floats

        Args:
            num (tuple): tuple with the input variable name and its value

        Raises:
            TypeError: input variable is neither an integer nor a float

        Returns:
            int: type-casted integer
        """

        var, val = num
        if not isinstance(val, (int, float)):
            raise TypeError(f"{var} must be an integer")
        else:
            return int(val)

    a = validate(("a", a))
    b = validate(("b", b))
    return a + b
