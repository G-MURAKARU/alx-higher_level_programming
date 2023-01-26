#!/usr/bin/python3

"""
    this is the ```4-print_square``` module.
    this module defines one function, print_square(size: int)
"""


def print_square(size: int) -> None:
    """
    print_square prints a square of side-length [size] using the # character

    Args:
        size (int): square's sides' length
    """

    def validate_size():
        """
        validate_size confirms that size is a positive integer

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    validate_size()

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
