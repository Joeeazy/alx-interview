#!/usr/bin/python3
"""Pascal's Triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n.
    """

    if not isinstance(n, int) or n <= 0:
        return []

    triangle = [[1] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, i):
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle[i].append(1)

    return triangle