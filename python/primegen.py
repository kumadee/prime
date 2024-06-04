#!/usr/bin/python3
"""Generate prime numbers"""

import math
from argparse import ArgumentParser


def is_prime(num: int) -> bool:
    last = int(math.sqrt(num)) + 1  # +1 as range is not inclusive of last
    if num > 2 and num % 2 == 0:
        return False
    for x in range(3, last, 2):
        if num % x == 0:
            return False
    return True


def count_prime(num: int, show: bool) -> int:
    count = 1
    for n in range(3, num, 2):
        if is_prime(n):
            count += 1
            if show:
                print(n)
    return count


if __name__ == "__main__":
    parser = ArgumentParser(description="Python Prime Sieve")
    parser.add_argument(
        "--limit", "-l", help="Upper limit for calculating prime numbers", type=int, default=1_000_000)
    parser.add_argument(
        "--show", "-s", help="Print found prime numbers", action="store_true")
    args = parser.parse_args()
    limit = args.limit

    prime_counts = {
        10: 4,                 # Historical data for validating our results - the number of primes
        100: 25,                # to be found under some limit, such as 168 primes under 1000
        1_000: 168,
        10_000: 1229,
        100_000: 9592,
        1_000_000: 78498,
        10_000_000: 664579,
        100_000_000: 5761455
    }
    c = count_prime(limit, args.show)
    print(f"Total primes for {limit} natural numbers is {c}.")
    result = c == prime_counts.get(limit, 0)
    print(f"Is number of prime correct? => {result}")
