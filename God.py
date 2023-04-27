def god() -> list:
    # write your code here
    class Human:
        def __init__(self, name):
            self.name = name

    class Man(Human):
        pass

    class Woman(Human):
        pass
    return [Man,Woman]


class Human:
    def __init__(self, name: str) -> None:
        self.name = name


class Man(Human):
    def __init__(self, name: str = "Adam") -> None:
        super().__init__(name)


class Woman(Human):
    def __init__(self, name: str = "Eva") -> None:
        super().__init__(name)


def god() -> list:
    # write your code here
    
    return [Man, Woman]