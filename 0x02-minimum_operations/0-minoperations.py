#!/usr/bin/python3
"""Module contains implementation of
minOperations(n) funtion.
"""


def minOperations(n: int) -> int:
    """Args-
           n: number of H characters
       returns:
           minimun number of operations
    """
    if n <= 1:
        return 0
    for ops in range(2, int(n ** 0.5) + 1):
        if n % ops == 0:
            return ops + minOperations(n // ops)
    return n
