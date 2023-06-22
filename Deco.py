class UnauthenticatedError(Exception):
    pass


class PermissionDeniedError(Exception):
    pass


def login_required(func: any) -> None:
    def wrapper(request: any) -> None:
        if "user" not in request:
            raise UnauthenticatedError("Authentication credentials were not provided!")
        return func(request)
    return wrapper


def admin_required(func: any) -> None:
    def wrapper(request: any) -> None:
        if "user" in request and request["user"].get("is_admin", False) is False:
            raise PermissionDeniedError("User must be admin!")
        return func(request)
    return wrapper


@admin_required
@login_required
def access_admin_page(request: dict) -> None:
    print(f"Welcome to the admin page, {request['user']['full_name']}")
