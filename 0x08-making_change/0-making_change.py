#!/usr/bin/python3
"""Module: 0-making_change"""


def makeChange(coin, total):
    """Determines the fewest number of coins needed to meet a given total"""
    if total <= 0:
        return 0
    coin = sorted(coin, reverse=True)  # sort the list in descending order
    count = 0

    for i in coin:
        if i > total:
            continue

        while total >= i:
            total -= i
            count += 1

    return - 1 if total != 0 else count
