#!/usr/bin/python3

def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    Args:
    coins (list): List of coin denominations.
    total (int): The total amount to make.
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for num in range(1, total + 1):
        for coin in coins:
            if num - coin >= 0:
                dp[num] = min(dp[num], dp[num - coin] + 1)

    return dp[total] if dp[total] != float('inf') else - 1
