#!/usr/bin/python3
"""
a method that calculates the fewest number of operations needed to result
"""


def minOperations(n):
    """
    returns the fewest number of operation need to result
    """
    x = 0
    y = 2
    while n > 1:
        while n % y == 0:
            x += y
            n = n / y
        y += 1
    return x
