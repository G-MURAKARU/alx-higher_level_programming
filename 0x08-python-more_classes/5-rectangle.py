#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """
    This is a class that defines a rectangle
    """

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """
        __init__ initialises a new Rectangle object

        Args:
            width (int, optional): rectangle's width. Defaults to 0.
            height (int, optional): rectangle's height. Defaults to 0.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self) -> int:
        """
        width retrieves the rectangle's width

        Returns:
            int: rectangle's width
        """

        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        width _summary_

        Args:
            value (int): the desired rectangle's width

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self) -> int:
        """
        height retrieves the rectangle's height

        Returns:
            int: rectangle's height
        """

        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        height _summary_

        Args:
            value (int): the desired rectangle's height

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self) -> int:
        """
        area finds the area of the rectangle

        Returns:
            int: rectangle's area
        """

        return self.__height * self.__width

    def perimeter(self) -> int:
        """
        perimeter finds the perimeter of the rectangle

        Returns:
            int: rectangle's perimeter
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        """
        __str__ defines the output when print() and str() are called on a
        rectangle object

        Returns:
            str: string representation of a rectangle
        """

        def _print() -> str:
            """
            my_print prints a rectangle

            Returns:
                str: string representation of a rectangle to be printed
            """

            rows: list[str] = []

            for _ in range(self.__height):
                string: str = ""
                for _ in range(self.__width):
                    string += "#"
                rows.append(string)

            rows[-1] = rows[-1][:-1]
            return "\n".join(rows)

        return "" if self.__width == 0 and self.__height == 0 else _print()

    def __repr__(self) -> str:
        """
        __repr__ returns object representation in string format

        Returns:
            str: rectangle object representation in string format
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        __del__ is called when a Rectangle instance is deleted
        """

        print("Bye Rectangle...")
