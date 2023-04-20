class Robot:
    def __init__(self, model: str, constructor: str, serial_no: int) -> None:
        self.model = model
        self.constructor = constructor
        self.serial_no = serial_no


def copy_robot(robot: Robot) -> Robot:
    # write your code here
    new_serial_no = robot.serial_no + 1
    return Robot(robot.model, robot.constructor, new_serial_no)

robot = Robot('g135', 'Alex', 1664)

print(copy_robot(robot)) 

"""
Creating a new class object with changes
"""