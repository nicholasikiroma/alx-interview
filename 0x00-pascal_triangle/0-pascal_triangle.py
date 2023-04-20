#!/usr/bin/python3
"""Module contains python function that models
   Pascal's Triangle.
"""


def pascal_triangle(n):
    """returns a list of lists of integers
        representing the Pascal’s triangle
    """
    if n <= 0 or n is None:
        return []

    triangle = [[1]]
    for i in range(1, n):
        rows = [1]
        for j in range(1, i):
            rows.append(triangle[i-1][j-1] + triangle[i-1][j])
        rows.append(1)
        triangle.append(rows)
    return triangle
