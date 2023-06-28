class InvalidUsername(Exception):
    pass


class PasswordMissmatch(Exception):
    pass


class ValidationError(Exception):
    pass


class DBUserCreationError(Exception):
    pass


def username_validation(username: str) -> None:
    
    if len(username) < 4 or len(username) > 15:
        raise InvalidUsername


def password_validation(password1: str, password2: str) -> None:
    if password1 != password2:
        raise PasswordMissmatch


def user_validation(user: dict) -> None:
    try:
        username_validation(user["username"])
        password_validation(user["password1"], user["password2"])
    except InvalidUsername:
        raise ValidationError
    except PasswordMissmatch:
        raise ValidationError


def db_user_creation(user: dict) -> str:
    try:
        user_validation(user)
    except ValidationError:
        raise DBUserCreationError
    else:
        print(f"{user['username']} is created in the database.")
