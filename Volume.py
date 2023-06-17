class Volume:
    def __get__(self, instance, owner):
        return instance.length * instance.width * instance.height

class Box:
    volume = Volume()
    def __init__(self, length: int, width: int, height: int) -> None:
        self.lenght = length
        self.width = width
        self.height = height