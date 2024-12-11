#!/usr/bin/python3
"""
Return: name of the player that won the most rounds
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): Array of integers for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"),
             or None if there is no clear winner.
    """
    if x < 1 or not nums:
        return None

    def sieve(n):
        """Generate a list of prime numbers up to n"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False
        return [i for i, prime in enumerate(is_prime) if prime]

    max_num = max(nums)
    primes = sieve(max_num)

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
