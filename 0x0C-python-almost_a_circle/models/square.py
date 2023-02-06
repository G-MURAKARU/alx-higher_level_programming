"""
    this is the `square` module
    this module defines one class, Square
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square defines properties of a Square object: attributes and methods

    Args:
        Rectangle (type): parent class
    """

    def __init__(
        self, size: int, x: int = 0, y: int = 0, id: int = None
    ) -> None:
        """
        __init__ is the square object's constructor

        Args:
            size (int): length square's sides
            x (int, optional): square x-coordinate. Defaults to 0.
            y (int, optional): square y-coordinate. Defaults to 0.
            id (int, optional): sqaure id number. Defaults to None.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self) -> int:
        """
        size gets the value of the square's side lengths

        Returns:
            int: length of square's side
        """

        return self.width

    @size.setter
    def size(self, value: int) -> None:
        """
        size sets the value of the square's side lengths

        Args:
            value (int): desired side length
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """
        update updates square's attributes
        """

        if args:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                elif idx == 1:
                    self.size = arg
                elif idx == 2:
                    self.x = arg
                elif idx == 3:
                    self.y = arg
        else:
            for attr, val in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, val)

    def to_dictionary(self) -> dict:
        """
        to_dictionary constructs a dictionary representation of a square object

        Returns:
            dict: square dict
        """

        attrs: set = {"id", "size", "x", "y"}

        return {
            attr: getattr(self, attr)
            for attr in self.__dir__()
            if attr in attrs
        }

    def __str__(self) -> str:
        """
        __str__ returns informal string representation of square object

        Returns:
            str: square string
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
