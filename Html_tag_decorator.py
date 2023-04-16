from typing import Callable, Any


def greeter(name: str) -> str:
    return f"Hello, {name}!"


def html_tag(tag: str) -> Callable:
    # write your code here
    def decor(func: None) -> Any:
        def wrapp(*args, **kwargs) -> str:
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        return wrapp
        
    return decor

@html_tag("div")
@html_tag("p")
def greeter(name: str) -> str:
    return f"Hello, {name}!"

print(greeter("Alex"))


"""
Напиши декоратор html_tag, який приймає строку tag. Він повинен обгортати результат обгорнутої функції.
Також повинно працювати послідовне декорування с декількома декораторами html_tag.
"""