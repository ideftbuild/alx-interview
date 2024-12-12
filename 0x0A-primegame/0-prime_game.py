#!/usr/bin/python3
from itertools import cycle


def is_prime(n):
    """Checks if a number is prime
    :returns: True if prime, False otherwise
    """
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    # Check divisors from 5 to sqrt(n), skipping even numbers
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:  # Check i and i + 2
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Determine the winner of a prime number removal game.

    Players take turns removing prime numbers and their multiples from
    a set of consecutive integers from 1 to n.

    Args:
        x (int): Number of rounds to play
        nums (list): List of upper limits for each round

    Returns:
        str or None: Name of the player who won the most rounds,
                     or None if tied
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Create a set of consecutive integers
        current_set = set(range(1, n + 1))

        # Alternate between Maria and Ben
        for player in cycle(['Maria', 'Ben']):
            # Find a valid prime move
            valid_move = False
            primes = sorted(num for num in current_set if is_prime(num))
            for prime in primes:
                # Remove the prime and its multiples
                multiples = {m for m in current_set if m % prime == 0}
                current_set -= multiples
                valid_move = True
                break

            # If no move possible, current player loses the round
            if not valid_move:
                if player == 'Maria':
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
