#!/usr/bin/python3

"""
    this is the ``2-matrix_divided`` module.
    the 2-matrix_divided module supplies two functions,
    validate_args(matrix: Any, div: Any) and
    matrix_divided(matrix: list[list[int|float]], div: int|float).
"""


def validate_args(matrix, div) -> bool:
    """
    validate_args validates input arguments using given criteria

    Args:
        matrix (Any): input matrix
        div (Any): input integer/floating-point number

    Returns:
        bool: whether arguments are valid or not
    """

    def validate_divisor():
        """
        validate_divisor validates that ``div`` is a non-zero int/float value

        Raises:
            TypeError: if ``div`` is neither of type int nor float
            ZeroDivisionError: if ``div`` is equal to zero
        """

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")

    def validate_matrix():
        """
        validate_matrix validates that the input matrix is a list of lists

        Raises:
            TypeError: if matrix if not of type list
            TypeError: if matrix is an empty list
            TypeError: if matrix is not strictly a list of lists
        """

        # if matrix is not a list
        if not isinstance(matrix, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        # if matrix is an empty list
        if not matrix:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        # if matrix is not a list of lists
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    def validate_matrix_dimensions():
        """
        validate_matrix_dimensions validates that all matrix rows
        are of the same length

        Raises:
            TypeError: if not all matrix rows are if the same length
        """

        # length should be same all through, use first row as reference
        length: int = len(matrix[0])

        # if any row length differs from first row length
        if any(len(row) != length for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    def validate_matrix_elements():
        """
        validate_matrix_elements validates that all matrix elements
        are of type int/float

        Raises:
            TypeError: if any matrix element is not of type int/float
        """

        # if a non-int/non-float element exists
        if not all(
            all(isinstance(ele, (int, float)) for ele in row)
            for row in matrix
        ):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    validate_divisor()
    validate_matrix()
    validate_matrix_dimensions()
    validate_matrix_elements()
    return True


def matrix_divided(matrix, div) -> list[list]:
    """
    matrix_divided divides all elements of the input ``matrix``
    by the input ``div``

    Args:
        matrix (list[list[int|float]]): input matrix of
            integers/floating-point numbers
        div (int|float): input divisor

    Returns:
        list[list[int|float]]: new matrix of resultant quotients
    """

    if validate_args(matrix, div):
        return [
            [round(element / div, 2) for element in row] for row in matrix
        ]
