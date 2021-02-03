"""
FizzBuzz module.
"""

import typing


class _Number:
    def __init__(self, integer: int):
        if integer < 0:
            raise ValueError('Argument must be a positive integer')
        self.integer = integer

    def _is_fizz(self):
        """
        Whether this is a 'fizz' number.
        """
        return self.integer % 3 == 0

    def _is_buzz(self):
        """
        Whether this is a 'buzz' number.
        """
        return self.integer % 5 == 0

    def __repr__(self) -> str:
        result = ''

        if self._is_fizz():
            result += 'fizz'

        if self._is_buzz():
            result += 'buzz'

        if not result:
            result = str(self.integer)

        return result


def _process_number(integer) -> str:
    return str(_Number(integer))


def process_range(till: int) -> typing.List[str]:
    """
    Returns a list of FizzBuzz numbers from 1 to limit.
    """
    result = []

    for i in range(1, till + 1):
        result.append(_process_number(i))

    return result
