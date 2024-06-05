#!/usr/bin/python3
"""Generate prime numbers"""

import math
import concurrent.futures
from argparse import ArgumentParser


def is_prime(num: int) -> bool:
    last = int(math.sqrt(num)) + 1  # +1 as range is not inclusive of last
    if num > 2 and num % 2 == 0:
        return False
    for x in range(3, last, 2):
        if num % x == 0:
            return False
    return True


def count_prime(start: int, num: int, show: bool) -> int:
    count = 0
    if start < 3:
        count = 1
        start = 3

    if start % 2 == 0:
        start += 1

    for n in range(start, num, 2):
        if is_prime(n):
            count += 1
            if show:
                print(n)
    return count


def create_chunks(num: int, num_of_chunks: int) -> list[tuple[int, int]]:
    result = []
    chunk_size = math.floor(num / num_of_chunks)
    for i in range(0, num_of_chunks):
        start = 1 if i == 0 else (i * chunk_size)
        end = (i + 1) * chunk_size
        if i + 1 == num_of_chunks:
            end += num % num_of_chunks
        result.append((start, end))
    return result


def process_chunks(chunk: tuple[int, int]) -> int:
    start, end = chunk
    # print(f"Process chunk ({start}, {end})")
    return count_prime(start, end, False)


if __name__ == "__main__":
    parser = ArgumentParser(description="Python Prime Sieve")
    parser.add_argument(
        "--limit",
        "-l",
        help="Upper limit for calculating prime numbers",
        type=int,
        default=1_000_000,
    )
    parser.add_argument(
        "--max-workers",
        "-w",
        help="Max worker threads for calculating prime numbers",
        type=int,
        default=4,
    )
    parser.add_argument(
        "--show", "-s", help="Print found prime numbers", action="store_true"
    )
    args = parser.parse_args()
    limit = args.limit

    prime_counts = {
        10: 4,  # Historical data for validating our results - the number of primes
        100: 25,  # to be found under some limit, such as 168 primes under 1000
        1_000: 168,
        10_000: 1229,
        100_000: 9592,
        1_000_000: 78498,
        10_000_000: 664579,
        100_000_000: 5761455,
    }
    chunks = create_chunks(args.limit, args.max_workers)
    total_prime_count = 0
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.max_workers
    ) as executor:
        for count in executor.map(process_chunks, chunks):
            total_prime_count += count
    print(f"Total primes for {limit} natural numbers is {total_prime_count}.")
    result = total_prime_count == prime_counts.get(limit, 0)
    print(f"Is number of prime correct? => {result}")