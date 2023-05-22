class Bike:
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    @classmethod
    def from_dict(cls, bike_dict: dict) -> "Bike":
        return cls(
            brand=bike_dict["brand"],
            model=bike_dict["model"],
            max_speed=bike_dict["max_speed"])


class MountainBike(Bike):
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        super().__init__(brand, model, max_speed)


class RoadBike(Bike):
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        super().__init__(brand, model, max_speed)






mountain_bike = MountainBike.from_dict({
    "model": "C2000",
    "brand": "Civia",
    "max_speed": 35,
})

print(isinstance(mountain_bike, MountainBike))
print(mountain_bike.brand)
print(mountain_bike.model)
print(mountain_bike.max_speed)