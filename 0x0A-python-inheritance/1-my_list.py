#!/usr/bin/python3

"""
    this is the ``1-my_list`` module.
    this module defines one class, MyList(list).
"""


class MyList(list):
    """
    MyList defines a List class based on the builtin list type

    Args:
        list (type): parent/base class
    """

    def __init__(self) -> None:
        """
        __init__ initialises an instance of the class;
        runs initialisation the parent class
        """

        super().__init__()

    def print_sorted(self):
        """
        print_sorted sorts a MyList list object in ascending order,
        using the 'sort' method from parent class 'list'
        """

        print(sorted(self))
