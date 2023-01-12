#!/usr/bin/python3

"""
    Defines a class MyList
"""


class MyList(list):
    def __init__(self) -> None:
        """
        __init__ initialises an instance of the class; runs initialisation the parent class
        """

        super().__init__()

    def print_sorted(self):
        """
        print_sorted sorts a MyList list object in ascending order,
        using the 'sort' method from parent class 'list'
        """

        print(sorted(self))
