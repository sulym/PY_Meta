class New_erorr(Exception):
    def __init__(self, name, responce) -> None:
        self.name = name
        self.responce = responce

    def __str__(self) -> str:
        return f"New error compleat"
    

def nw_err(ls: list) -> None:
    try:
        if len(ls) == 2:
            raise New_erorr("Custom Error", "sdsdsd")  # Вызываем пользовательское исключение
    except New_erorr as e:  # Указываем, какую ошибку мы хотим отловить
        print(e)


print(nw_err(ls=[1,2]))