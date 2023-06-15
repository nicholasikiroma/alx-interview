#!/usr/bin/python3
"""ALX Interview Task"""


def makeChange(coins, total):
    """Computes the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible"""
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        if total % coin == 0:
            coin_count += total // coin
            return coin_count
        if total >= coin:
            count = total // coin
            coin_count += count
            total -= coin * count

    return -1 if total > 0 else coin_count
