#!/usr/bin/python3
"""ALX Interview Task"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    sieve = [True] * (n + 1)
    prime = []
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    Maria = Ben = 0
    for _ in range(x):
        prime = primes(nums[_])
        if len(prime) % 2:
            Maria += 1
        else:
            Ben += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
