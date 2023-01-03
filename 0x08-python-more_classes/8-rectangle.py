#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """
    This is a class that defines a rectangle
    """

    number_of_instances: int = 0
    print_symbol = "#"

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """
        __init__ initialises a new Rectangle object

        Args:
            width (int, optional): rectangle's width. Defaults to 0.
            height (int, optional): rectangle's height. Defaults to 0.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

        Rectangle.number_of_instances += 1

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
                    symbol = Rectangle.print_symbol
                    if not isinstance(symbol, str):
                        symbol = str(symbol)
                    string += symbol
                rows.append(string + "\n")

            rows[-1] = rows[-1][:-1]
            return "".join(rows)

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

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal returns the bigger rectangle based on area

        Args:
            rect_1 (Rectangle): first rectangle to compare
            rect_2 (Rectangle): second rectangle to compare

        Raises:
            TypeError: raised if either input is not a Rectangle instance

        Returns:
            Rectangle: the larger rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_2 if rect_2.area() > rect_1.area() else rect_1
