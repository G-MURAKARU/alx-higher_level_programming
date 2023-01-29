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

    def to_json(self, attrs=None) -> dict:
        """
        to_json gets a dictionary representation of a Student object

        Returns:
            dict: dictionary representation of Student object
        """

        if (
            attrs
            and isinstance(attrs, list)
            and all(isinstance(ele, str) for ele in attrs)
        ):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

        return self.__dict__

    def reload_from_json(self, json: dict) -> None:
        """
        reload_to_json replace all Student attributes

        Args:
            json (dict): key/value pairs to replace attributes with
        """

        for key, value in json.items():
            setattr(self, key, value)
