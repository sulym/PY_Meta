class Cycle:
    
    def __init__(self, ls: list) -> None:
        self.ls = ls

    def __iter__(self):
        self.cur_elment = 0
        return self
    
    def __next__(self):
        if len(self.ls) == 0:
            raise StopIteration
        result = self.ls[self.cur_elment]
        self.cur_elment += 1
        self.cur_elment %= len(self.ls)
        return result

lsss = [0, 1, 2, 3]
each = Cycle(lsss)

iterator = iter(each)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Итератор бесконечно повторяет элементы списка в том же порядке.
# Когда мы достигаем конца списка, индекс self.cur_element обнуляется, и итерация начинается сначала.

##### M #####

from __future__ import annotations
from typing import Iterable, Union


class Cycle:
    def __init__(self, iterable: Iterable) -> None:
        self.iterable = iterable

    def __iter__(self) -> Cycle:
        self.current_index = 0
        return self

    def __next__(self) -> Union[int, str, StopIteration]:
        if not self.iterable:
            raise StopIteration

        res = self.iterable[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.iterable)

        return res