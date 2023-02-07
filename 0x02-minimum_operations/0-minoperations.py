#!/usr/bin/python3
"""
a method that calculates the fewest number of operations needed to result
"""


def minOperations(n):
    """
    returns the fewest number of operation need to result
    """
    p = 0

    if n <= 1:
        return p

    for i in range(2, n + 1):
        while (0 == n % i):
            p = p + i
            n = n / i
            if n < i:
                break
    return
