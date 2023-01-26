#!/usr/bin/python3


"""
    this is the ``3-say_my_name`` module.
    the say_my_name module provides one function,
    say_my_name(first_name: str, second_name: str = "")
"""


def say_my_name(first_name: str, second_name: str = "") -> None:
    """
    say_my_name prints a string with input name

    Args:
        first_name (str): first name to print
        second_name (str, optional): second name/surname to print. Defaults to "".
    """

    def validate_input(inpt: tuple) -> None:
        """
        validate_input validates that input arguments are all strings

        Args:
            inpt (tuple): contains argument name and argument value

        Raises:
            TypeError: if any input argument is not a string
        """

        var, val = inpt
        if not isinstance(val, str):
            raise TypeError(f"{var} must be a string")

    validate_input(("first_name", first_name))
    validate_input(("second_name", second_name))

    print(f"My name is {first_name} {second_name}")
