class Robot:
    def __init__(self, wheels: int, gears: int, pistons: int) -> None:
        self.wheels = wheels
        self.gears = gears
        self.pistons = pistons
robots = [
  Robot(wheels=10, gears=18, pistons=16),
  Robot(wheels=4, gears=8, pistons=8),
  Robot(wheels=22, gears=17, pistons=30),
]


def robots_parts(robots: list) -> dict:
    # write your code here
    new_dict = {"wheels": 0, "gears": 0, "pistons": 0}
    for i in robots:
        new_dict["wheels"] += i.wheels
        new_dict["gears"] += i.gears
        new_dict["pistons"] += i.pistons
        
    return new_dict

print(robots_parts(robots))


"""
Є клас Robot, його метод __init__ приймає кількість частин із яких він виготовляється: 
wheels, gears, pistons і зберігає їх у властивостях відповідно.

Напиши функцію robots_parts, яка приймає список з екземплярами класу Robot,
підраховує суму частин різного виду, записує її в словник з ключами 
'wheels', 'gears', 'pistons' та повертає його.
"""