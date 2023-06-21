from typing import Any


def find_mode(ls: list[Any]) -> Any:
    # write your code here
    if not isinstance(ls, list):
        raise TypeError ("ls must be a list")

    if len(ls) == 0:
        raise ValueError ("ls must be non-empty")

    return max(ls, key=ls.count)

print(find_mode(ls=[5, "hello", 12, 33, "a", 12, "a", "a"]))

### m ###

from statistics import mode
from typing import Any


def find_mode(ls: list[Any]) -> Any:
    if not isinstance(ls, list):
        raise TypeError("ls must be a list")
    if len(ls) == 0:
        raise ValueError("ls must be non-empty")
    return mode(ls)

