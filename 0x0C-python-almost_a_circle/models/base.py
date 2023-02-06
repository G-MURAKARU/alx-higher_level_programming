#!/usr/bin/python3

"""
    this is the `base` module
    this module defines one class, Base
"""

import json


class Base:
    """
    defines properties of a Base object: its attributes and methods
    """

    __nb_objects = 0

    def __init__(self, id: int = None) -> None:
        """
        __init__ is the Base object's constructor

        Args:
            id (int, optional): object's id number. Defaults to None.
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: list[dict]) -> str:
        """
        to_json_string finds JSON string representation of `list_dictionaries`

        Args:
            list_dictionaries (list[dict]): list of dicts

        Returns:
            str: JSON string
        """

        return (
            json.dumps(list_dictionaries)
            if list_dictionaries and len(list_dictionaries)
            else "[]"
        )

    @staticmethod
    def from_json_string(json_string: str) -> list[dict]:
        """
        from_json_string derives python list from `json_string`

        Args:
            json_string (str): input JSON string

        Returns:
            list[dict]: list of dicts
        """

        return (
            json.loads(json_string)
            if json_string and isinstance(json_string, str)
            else []
        )

    @classmethod
    def save_to_file(cls, list_objs: list[type]) -> None:
        """
        save_to_file writes JSON string of `list_objs` to a file

        Args:
            list_objs (type): list of instances that inherit from `Base`
        """

        filename: str = f"{cls.__name__}.json"
        if list_objs:
            objs = [
                json.loads(cls.to_json_string(obj.to_dictionary()))
                for obj in list_objs
            ]
        with open(file=filename, mode="w") as my_file:
            json.dump(objs, my_file)

    @classmethod
    def create(cls, **dictionary):
        """
        create _summary_
        """

        from .rectangle import Rectangle
        from .square import Square

        if cls.__name__ == "Rectangle":
            obj = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            obj = Square(5)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls) -> list:
        """
        load_from_file loads JSON class instances from file

        Returns:
            list: list of loaded class instances
        """

        filename: str = f"{cls.__name__}.json"

        try:
            with open(file=filename, mode="r", encoding="utf-8") as my_file:
                content = cls.from_json_string(my_file.read())
        except FileNotFoundError:
            return []

        return [cls.create(**instance) for instance in content]
