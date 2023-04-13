from functools import wraps
from typing import Callable, Any


def bread(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print("</--------\\>")
        func(*args, **kwargs)
        print("<\\________/>")

    return wrapper


def ingredients(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(" #tomatoes#")
        func(*args, **kwargs)
        print("   ~salad~")

    return wrapper


# write your code here
def sandwich():
    # write your code here
    pass