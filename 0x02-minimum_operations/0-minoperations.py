#!/usr/bin/python3
"""Module: 0-minoperations"""
from functools import reduce


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters """
    if n <= 1:
        return 0
    return sum(prime_factors(n))


def prime_factors(n):
    """Get the prime factors of n and return the sum of factors"""
    factors = []
    divisor = 2

    # Try dividing n by 2 (smallest prime) until it no longer divides
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor

    # Check odd numbers starting from 3
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2

    # If n is still greater than 2, it is prime
    if n > 2:
        factors.append(n)

    return factors
