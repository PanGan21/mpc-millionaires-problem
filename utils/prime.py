import random
from Crypto.Util.number import getRandomNBitInteger

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


def gen_prime(n):
    """
    Generate a prime number with n bits using a probabilistic method.

    Args:
        n (int): The number of bits for the prime number.

    Returns:
        int: A prime number with n bits.
    """
    while True:
        p = getRandomNBitInteger(n)
        p |= 1  # we only want odd numbers
        if is_prime(p):
            return p
        print('.', end='', flush=True)


def egcd(aa, bb):
    """
    Extended Euclidean Algorithm to calculate the greatest common divisor (GCD)
    and Bezout coefficients of two integers.

    Args:
        aa (int): The first integer.
        bb (int): The second integer.

    Returns:
        Tuple[int, int, int]: A tuple containing the GCD and Bezout coefficients (x, y).
    """
    lr, r = abs(aa), abs(bb)
    x, lx, y, ly = 0, 1, 1, 0
    while r:
        lr, (q, r) = r, divmod(lr, r)
        x, lx = lx - q*x, x
        y, ly = ly - q*y, y
    return lr, lx * (-1 if aa < 0 else 1), ly * (-1 if bb < 0 else 1)


def modinv(a, m):
    """
    Modular multiplicative inverse of a modulo m.

    Args:
        a (int): The integer for which the modular inverse is to be found.
        m (int): The modulus.

    Returns:
        int: The modular inverse of a modulo m.

    Raises:
        ValueError: If a and m are not coprime.
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
