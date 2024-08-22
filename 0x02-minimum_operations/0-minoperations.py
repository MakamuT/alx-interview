#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed to
result in exactly n H characters in the file
"""


def minOperations(n):
    if n <= 1:
        return 0
    op = 0
    fac = 2

    while n > 1:
        if n % fact == 0:
            while n % factor == 0:
                n = n / fac
                op += fac
        factor += 1
    return op
