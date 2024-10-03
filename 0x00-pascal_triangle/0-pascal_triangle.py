#!/usr/bin/python3
"""
Module: 0-pascal_triangle
"""


def pascal_triangle(n: int) -> list[list[int]]:
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # Initialize the edges with 1 and compute the inner elements of the row
        row = [1] + [triangle[i - 1][j - 1] + triangle[i - 1][j]
                     for j in range(1, i)] + [1] if i != 0 else []
        # Add the row to the final triangle
        triangle.append(row)

    return triangle
