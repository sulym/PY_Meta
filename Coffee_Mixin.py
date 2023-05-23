class Espresso:
    def __init__(self) -> None:
        self.cup_with_coffee = []

    def add_coffee(self) -> None:
        self.cup_with_coffee.append("Coffee")

    def add_water(self) -> None:
        self.cup_with_coffee.append("Hot water")

    def add_sugar(self) -> None:
        self.cup_with_coffee.append("Sugar")

    def add_milk(self) -> None:
        """
        No milk provided in espresso
        """

    def make_coffee(self) -> list:
        self.add_coffee()
        self.add_water()
        self.add_sugar()
        self.add_milk()
        return self.cup_with_coffee


class CaffeineFreeMixin:
    def add_coffee(self) -> None:
        self.cup_with_coffee.append("Caffeine free coffee")

class DoubleWaterMixin:
    def add_water(self) -> None:
        self.cup_with_coffee.append("Hot water x2")

class NoSugarMixin:
    def add_sugar(self) -> None:
        self.cup_with_coffee.append()

class MilkMixin:
    def add_milk(self) -> None:
        self.cup_with_coffee.append("Milk")

class Americano(DoubleWaterMixin, Espresso):
    pass
class CaffeineFreeEspresso(CaffeineFreeMixin, Espresso):
    pass
class NoSugarMilkEspresso(NoSugarMixin, MilkMixin, Espresso):
    pass
class CaffeineFreeNoSugarMilkAmericano(CaffeineFreeMixin,DoubleWaterMixin, NoSugarMixin, MilkMixin, Espresso):
    pass
