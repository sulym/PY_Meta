def create_permissions(users: list) -> None:
    for user in users:
        print(f'Creating permissions for {user["username"]}')


def only_admin(func: list) -> None:
    # write your code here
    def wrapper(*args, **kwargs) -> None:
        new_ls = []
        for i in args:
            for k in i:
                if k["is_admin"] is True:
                    new_ls.append(k)
            return func(new_ls)
                
    return wrapper

users = [
     {'username': 'admin', 'is_admin': True},
     {'username': 'moderator_a11', 'is_admin': True},
     {'username': 'custom_user1', 'is_admin': False},
     {'username': 'custom_user2', 'is_admin': False},
     {'username': 'admin_2nd', 'is_admin': True},
]

@only_admin
def create_permissions(users: list) -> None:
    for user in users:
        print(f'Creating permissions for {user["username"]}')


print(create_permissions(users))


