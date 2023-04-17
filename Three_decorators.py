from typing import Callable

"""
Напиши 3 декоратори arrow, number_filter, round_dict, такі що:

arrow перетворює вхідний словник у список рядків виду 'key -> value'.
number_filter фільтрує вхідний список і залишає тільки числові типи
round_dict округлює числа у вхідному списку і створює словник, 
де ключ - це нове значення числа, а його значення - подвоєне нове значення числа.
Задекоруй функцію like_numbers трьома декораторами у правильному порядку так,
щоб отримати результат показаний у прикладі.
"""

def arrow(func: Callable):
    def inner(items: dict, *args, **kwargs):
        return func([f"{key} -> {value}" for key, value in items.items()])
    return inner

def number_filter(func: Callable):
    def inner_1(items: list, *args, **kwargs):
        return func([item for item in items if type(item) == int or type(item) == float])
    return inner_1


def round_dict(func: Callable):
    def inner_2(items, *args, **kwargs):
        return func({round(item): round(item)*2 for item in items})
    return inner_2


items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]


# Decorate this function with 3 decorators above in a correct order
@number_filter
@round_dict
@arrow
def like_numbers(items: list) -> str:
    return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"

print(like_numbers(items))