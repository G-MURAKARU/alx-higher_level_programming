"""
    this is the ``2-matrix_divided`` module.
    the 2-matrix_divided module supplies one function, matrix_divided(matrix: list[list[int|float]], div: int|float).
"""


def matrix_divided(
    matrix: list[list[int | float]], div: int | float
) -> list[list[int | float]]:
    """
    matrix_divided divides all elements of the input ``matrix`` by the input ``div``

    Args:
        matrix (list[list[int | float]]): input matrix of integers/floating-point numbers
        div (int | float): input divisor

    Returns:
        list[list[int|float]]: new matrix of resultant quotients
    """

    def validate_divisor(div):
        """
        validate_divisor validates that ``div`` is a non-zero int/float value

        Args:
            div (Any): input divisor to validate
        """

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")

    def validate_matrix(matrix):
        """
        validate_matrix validates that the input matrix is a list of lists

        Args:
            matrix (Any): input matrix to validate
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
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    def validate_matrix_elements(matrix):
        """
        validate_matrix_elements validates that all matrix elements are of type int/float

        Args:
            matrix (list[list[int|float]]): input matrix to validate
        """

        # if a non-int/non-float element exists
        for row in matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats"
                    )

    def validate_matrix_dimensions(matrix):
        """
        validate_matrix_dimensions validates that all matrix rows are of the same length

        Args:
            matrix (list[list[int|float]]): input matrix to validate
        """

        # length should be same all through, use first row as reference
        length: int = len(matrix[0])

        # if any row length differs from first row length
        for row in matrix:
            if len(row) != length:
                raise TypeError("Each row of the matrix must have the same size")

    validate_divisor(div)
    validate_matrix(matrix)
    validate_matrix_dimensions(matrix)
    validate_matrix_elements(matrix)

    new_matrix: list[list[int | float]] = []

    for row in matrix:
        new_row: list[int | float] = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix


# if __name__ == "__main__":
#     matrix = [[7, -14, 21], [-3.5, 4.9, 6.3], [9.3, 15, -12.7]]
#     print(matrix_divided(matrix, 7))
