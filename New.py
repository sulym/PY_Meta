class FirstClass:
    def __init__(self, *args, **kwargs) -> None:
        self.new_arg = args
        self.new_kwarg = kwargs

makra = FirstClass("makra", rass="human", age=25)

print(makra)