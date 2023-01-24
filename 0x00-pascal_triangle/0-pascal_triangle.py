#!/usr/bin/python3
"""
Print Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a Pascal's triangle
    in a list of list
    """
    angle = []
    if type(n) is not int or n <= 0:
        return angle
    for i in range(n):
        line = []
        for a in range(i + 1):
            if a == 0 or a == i:
                line.append(1)
            elif i > 0 and a > 0:
                line.append(angle[i - 1][a - 1] + angle[i - 1][a])
        angle.append(line)
    return angle
