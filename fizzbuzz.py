"""
FizzBuzz module.
"""

import typing


class _Number:
    def __init__(self, integer: int):
        if integer < 0:
            raise ValueError('Argument must be a positive integer')
        self.integer = integer

    def is_fizz(self):
        """
        Whether this is a 'fizz' number.
        """
        return self.integer % 3 == 0

    def is_buzz(self):
        """
        Whether this is a 'buzz' number.
        """
        return self.integer % 5 == 0

    def is_fizzbuzz(self):
        """
        Whether this is a 'fizzbuzz' number.
        """
        return self.is_fizz() and self.is_buzz()

    def __repr__(self) -> str:
        result = ''

        if self.is_fizz():
            result += 'fizz'

        if self.is_buzz():
            result += 'buzz'

        if not result:
            result = str(self.integer)

        return result


def generate(till: int) -> typing.List[str]:
    """
    Returns a list of FizzBuzz numbers from 1 to limit.
    """
    result = []

    for i in range(1, till + 1):
        result.append(str(_Number(i)))

    return result
