class Grade:
    def __init__(self, minvalue: int = 2, maxvalue: int = 12):
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.protected_name = None

    def __set_name__(self, owner, name):
        self.protected_name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.protected_name]
    
    def __set__(self,instance, value):
        if not isinstance(value, int):
            raise TypeError("Grade should be integer")
        if value < self.minvalue or value > self.maxvalue:
            raise ValueError(f"Grade should not be less than {self.minvalue} and greater than {self.maxvalue}")
        instance.__dict__[self.protected_name] = value



class SchoolDiary():
    math = Grade()
    history = Grade()
    literature = Grade()

    def __init__(self, math: int, history: int, literature: int) -> None:
        self.math = math
        self.history = history
        self.literature = literature


### m ###

class Grade:
    def __init__(self) -> None:
        self.minvalue = 2
        self.maxvalue = 12

    def __set_name__(self, owner, name) -> None:
        self.protected_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.protected_name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Grade should be integer")
        if value not in range(self.minvalue, self.maxvalue + 1):
            raise ValueError(
                f"Grade should not be less than {self.minvalue} and greater than {self.maxvalue}"
            )
        setattr(instance, self.protected_name, value)


class SchoolDiary:
    math = Grade()
    history = Grade()
    literature = Grade()

    def __init__(self, math: int, history: int, literature: int) -> None:
        self.math = math
        self.history = history
        self.literature = literature
