#!/usr/bin/python3

"""
    this is the `rectangle` module
    this module defines one class, Rectangle
"""

from .base import Base


class Rectangle(Base):
    """
    Rectangle defines the attributes and methods of a Rectangle object

    Args:
        Base (type): parent class
    """

    def __init__(
        self, width: int, height: int, x: int = 0, y: int = 0, id: int = None
    ) -> None:
        """
        __init__ is the Rectangle object's constructor

        Args:
            width (int): rectangle width
            height (int): rectangle heigth
            x (int, optional): rectangle x-coordinate. Defaults to 0.
            y (int, optional): rectangle y-coordinate. Defaults to 0.
            id (int, optional): rectangle id number. Defaults to None.
        """

        super().__init__(id)

        variables = ("width", "height", "x", "y")
        values = (width, height, x, y)
        for var, val in zip(variables, values):
            self.validate_value(var=var, val=val)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self) -> int:
        """
        gets the `__width` private instance attribute

        Returns:
            int: value of `__width`
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the `__width` private instance attribute

        Args:
            value (int): desired `__width` value
        """

        self.validate_value("width", value)
        self.__width = value

    @property
    def height(self) -> int:
        """
        gets the `__height` private instance attribute

        Returns:
            int: value of `__height`
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the `__height` private instance attribute

        Args:
            value (int): desired `__height` value
        """

        self.validate_value("height", value)
        self.__height = value

    @property
    def x(self) -> int:
        """
        gets the `__x` private instance attribute

        Returns:
            int: value of `__x`
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the `__x` private instance attribute

        Args:
            value (int): desired `__x` value
        """

        self.validate_value("x", value)
        self.__x = value

    @property
    def y(self) -> int:
        """
        gets the `__y` private instance attribute

        Returns:
            int: value of `__y`
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the `__y` private instance attribute

        Args:
            value (int): desired `__y` value
        """

        self.validate_value("y", value)
        self.__y = value

    def area(self) -> int:
        """
        area finds the geometric area of the rectangle

        Returns:
            int: rectangle's area
        """

        return self.width * self.height

    def display(self) -> None:
        """
        display prints rectangle on stdout using `#` character
        """
        from itertools import chain

        rectangle: str = "".join(
            chain(
                ("\n" for _ in range(self.y)),
                (
                    ((" " * self.x) + ("#" * self.width) + "\n")
                    for _ in range(self.height)
                ),
            )
        )
        print(rectangle, end="")

    def update(self, *args, **kwargs) -> None:
        """
        update updates the rectangle object's attributes
        """

        if args:
            from contextlib import suppress

            with suppress(IndexError):
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for attr, val in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, val)

    def to_dictionary(self) -> dict:
        """
        to_dictionary constructs a dictionary representation of a rectangle object

        Returns:
            dict: rectangle dict
        """

        attrs: set = {"id", "width", "height", "x", "y"}

        return {
            attr: getattr(self, attr)
            for attr in self.__dir__()
            if attr in attrs
        }

    def __str__(self) -> str:
        """
        __str__ returns informal string representation of rectangle object

        Returns:
            str: rectangle string
        """

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    @staticmethod
    def validate_value(var: str, val: int):
        """
        validate_value validates input arguments

        Args:
            var (str): name of variable
            val (int): value stored in variable

        Raises:
            TypeError: if `val` is not of type int
            ValueError: if `var` is `x` or `y` and is < 0
            ValueError: if `var` is `width` or `height` and is <= 0
        """

        if type(val) != int:
            raise TypeError(f"{var} must be an integer")

        if var in {"x", "y"}:
            if val < 0:
                raise ValueError(f"{var} must be >= 0")
        elif val <= 0:
            raise ValueError(f"{var} must be > 0")
