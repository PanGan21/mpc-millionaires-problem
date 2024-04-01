import random

# generate with generator.py
PRIMES_FILE = "primes.txt"


def load_small_primes():
    """
    Load small prime numbers from the PRIMES_FILE.

    Returns:
        list: A list of small prime numbers.
    """
    return list(map(int, map(str.strip, open(PRIMES_FILE, 'r').readlines())))


def is_prime(n, k=40):
    """
        Uses the Miller-Rabin primality test to check if a number is prime.
        https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

        Args:
            n (int): The number to check for primality.
            k (int): The number of iterations for the Miller-Rabin test.

        Returns:
            bool: True if the number is prime, False otherwise.
    """
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True
