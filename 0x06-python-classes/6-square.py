#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    This is a class that defines a square
    """

    def __init__(self, size: int = 0, position=(0, 0)) -> None:
        """
        __init__ Initialises a new Square instance

        Args:
            size (int, optional): the square's sides' length. Defaults to 0.
            position (tuple[int, int], optional): square's coordinates.
                                                  Defaults to (0, 0).

        Raises:
            TypeError: raised if the passed size argument is not an integer
            ValueError: raised if the passed size argument is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size: int = size

        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not all(isinstance(num, int) for num in position)
            or any(num < 0 for num in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    @property
    def size(self):
        """
        size is a getter for the private size instance attribute

        Returns:
            size (int): length of sides
        """
        return self.__size

    @size.setter
    def size(self, custom_size: int):
        """
        size is a setter for the private size instance attribute

        Args:
            custom_size (int): size to assign to size instance attribute

        Raises:
            TypeError: raised if the passed custom_size argument is not an int
            ValueError: raised if the passed custom_size argument < 0
        """

        if not isinstance(custom_size, int):
            raise TypeError("size must be an integer")

        if custom_size < 0:
            raise ValueError("size must be >= 0")

        self.__size = custom_size

    @property
    def position(self):
        """
        position is a getter for the private position instance attribute

        Returns:
            position: the square's (x, y) position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position is a setter for the square's (x, y) position

        Args:
            value (_type_): a tuple of 2 integers

        Raises:
            TypeError: raised if value is not a tuple of integers
        """

        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or any(num < 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        area finds the area of a square instance
        """
        return self.__size**2

    def my_print(self):
        """
        my_print prints the square
        """

        def _my_print():
            """
            _my_print prints the square if size > 0
            """
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()

        print() if self.__size == 0 else _my_print()
