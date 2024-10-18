#!/usr/bin/python3
"""Module: 0-minoperations"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters """
    from itertools import cycle

    if n <= 0:
        return 0

    num_ops = 0
    count: int = 1
    copied: int = 0
    for op in cycle(['p', 'c', 'p']):
        if op == 'p':
            count += copied
        else:
            copied = count
        num_ops += 1

        if count >= n or count + copied >= n:
            break

    return num_ops
