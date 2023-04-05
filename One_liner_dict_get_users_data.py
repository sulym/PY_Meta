users = [
            (12, 'Maxim', 'maxim@example.com', 'UBg11eub42hge'),
            (13, 'Dmitro', 'dmitro@example.com', 'sdTioT36723fw'),
            (14, 'Roman', 'roman@example.com', 'hbFEkj34NggE2'),
            (15, 'Ivan', 'ivan@example.com', 'sdTioT36723fw'),
        ]

def get_users_data(users: list) -> dict:
    # write your code here
    return {dat[0]: {"username": dat[1], "email": dat[2], "password": dat[3]} for dat in users}

print(get_users_data(users))