from typing import Callable


def send_secure_information(user: dict) -> None:
    print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")


def admin_required(func: Callable) -> None:
    # write your code here
    def atribut(*args, **kwargs):
        if not args[0].get('is_admin')  :
            print("# You are not allowed to see this information!")
        else:
            func(*args, **kwargs)
    return atribut

@admin_required
def send_secure_information(user: dict) -> None:
    print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")

print(send_secure_information({'name': "Administrator", 'is_admin': False}))


##### M #####

from typing import Callable, Any


def send_secure_information(user: dict) -> None:
    print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")


def admin_required(func: Callable) -> Callable:
    def wrapper(user: dict) -> Any:
        if user["is_admin"]:
            return func(user)

        print("You are not allowed to see this information!")

    return wrapper