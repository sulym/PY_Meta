"""
Реалізуй функцію numbers_handler, яка приймає список чисел numbers і три колбеки:

before - колбек, який першим викликається для кожного з чисел
action - викликається другим для кожного з чисел
after - викликається останнім для кожного з чисел
Кожен із колбеків має єдиний параметр - число number
"""


def new_number(number: int) -> str:
    print(f"Received a new number: {number}")


def is_positive(number: int) -> str:
    if number > 0:
        print(f"{number} is a positive number")
    if number < 0:
        print(f"{number} is a negative number")
    if number == 0:
        print("Zero")


def print_bye(number: int) -> str:
    print("Bye!")


def numbers_handler(
    numbers: list,
    before: callable = new_number,
    action: callable = is_positive,
    after: callable = print_bye,
) -> None:
    for num in numbers:
        before(num)
        action(num)
        after(num)

print(numbers_handler([1,2,3,4], before=new_number, action=is_positive, after=print_bye))

#### Mentor####

from typing import Callable


def new_number(number: int) -> None:
    print(f"Received a new number: {number}")


def is_positive(number: int) -> None:
    if number > 0:
        print(f"{number} is a positive number")
    elif number == 0:
        print("Zero")
    else:
        print(f"{number} is a negative number")


def print_bye(number: int) -> None:
    print("Bye!")


def numbers_handler(
    numbers: list,
    before: Callable = new_number,
    action: Callable = is_positive,
    after: Callable = print_bye,
) -> None:
    for number in numbers:
        before(number)
        action(number)
        after(number)