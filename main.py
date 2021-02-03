#!/usr/bin/env python3

"""
FizzBuzz CLI
"""

import sys

from lib.fizzbuzz import process_range as fizzbuzz_range


def main():
    """
    Main
    """
    result = fizzbuzz_range(_get_limit())
    print("\n".join(result))


def _get_limit() -> int:
    try:
        limit = int(sys.argv[1])

        if limit < 0:
            raise ValueError

        return limit
    except (IndexError, ValueError):
        print('Argument 1 must be a positive integer.')
        sys.exit(1)


if __name__ == '__main__':
    main()
