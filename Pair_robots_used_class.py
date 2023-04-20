
robots = [
  'Alex',
  'Tom'
]

class Robot:
    # write your code here
    def __init__(self, name: str) -> None:
        self.name = name
        self.partner = None

def pair_robots(robots: list) -> tuple:
    # write your code here
    robot1 = Robot(robots[0])
    robot2 = Robot(robots[1])
    robot1.partner = robots[1]
    robot2.partner = robots[0]
    return robot1, robot2

print(pair_robots(robots))


"""
Створи клас Robot, метод __init__ якого приймає тільки name
та записує його у властивість self.name, a властивість self.partner спочатку None.
Створи функцію pair_robots, яка приймає список з двох імен, створює для кожного екземпляр класу Robot 
та додає до кожного властивість partner з посиланням на партнера (інший об'єкт). Функція повертає кортеж з роботами.
"""