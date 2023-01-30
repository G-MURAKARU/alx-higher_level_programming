#!/usr/bin/python3

"""
    this is the ``12-pascal_triangle`` module.
    this module provides one function, pascal_triangle(n: int).
"""


def pascal_triangle(n: int) -> list[list[int]]:
    """
    pascal_triangle generates Pascal's triangle to the nth level

    Args:
        n (int): level to generate

    Returns:
        list[list[int]]: list representation of generated triangle
    """

    from copy import copy

    if n <= 0:
        return []

    triangle = [[1]]

    for counter in range(1, n):
        next_row = copy(triangle[counter - 1])
        next_row.insert(0, 0)
        next_row.append(0)
        i = 0
        j = []
        while i < len(next_row) - 1:
            j.append(next_row[i] + next_row[i + 1])
            i += 1
        triangle.append(j)
    return triangle


if __name__ == "__main__":
    print(pascal_triangle(10))
