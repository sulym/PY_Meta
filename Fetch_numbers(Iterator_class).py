from __future__ import annotations
from typing import Iterator, Union


class NumberIterator:
    def __init__(self, numbers: list) -> None:
        self.numbers = numbers

    def __iter__(self) -> NumberIterator:
        self.it = 0
        return self

    def __next__(self) -> Union[int, StopIteration]:
        if self.it >= len(self.numbers):
            raise StopIteration
        result = self.numbers[self.it]
        self.it += 1
        return result


def fetch_numbers(iterator: Iterator, number: int) -> list:
    ls = []
    for i in range(number):
        ls.append(next(iterator))
    return ls
        


iter_ = iter(NumberIterator([1, 2, 3, 4, 5]))

print(fetch_numbers(iterator=iter_, number=3))