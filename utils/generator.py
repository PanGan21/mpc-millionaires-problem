"""
generator.py - Prime Number Generator

This script generates prime numbers up to a specified limit and writes them to a file.

Usage:
    To run this script, execute the following command in your terminal:
    python utils/generator.py

    Make sure you have Python installed on your system.

    The generated prime numbers will be written to the file specified by the PRIMES_FILE variable.

    Note: This script requires the prime.py module to be present in the 'utils' directory.
"""

import math
from prime import PRIMES_FILE

wow = [2]

with open(PRIMES_FILE, "w") as file:
    for i in range(3, 2000000):
        is_prime = True
        for p in wow:
            if p > int(math.sqrt(i)) + 1 or p > i:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            wow.append(i)
            file.write(str(i) + "\n")
