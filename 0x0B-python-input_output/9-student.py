#!/usr/bin/python3

"""
    this is the ``9-student`` module.
    this module defines one class, Student.
"""


class Student:
    """
    Student class defines a student object, its attributes and methods
    """

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """
        __init__ is the Student object constructor

        Args:
            first_name (str): student's first name attribute
            last_name (str): student's last name attribute
            age (int): student's age attribute
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self) -> dict:
        """
        to_json _summary_

        Returns:
            dict: dictionary representation of Student object
        """
        return self.__dict__
