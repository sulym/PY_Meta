robot1 = {'chip_ver': 'M1', 'serial_no': 1}
robot2 = {'serial_no': 2, 'chip_ver': 'M1','serial_no': 2}

def compare_robots(robot1: dict, robot2: dict) -> bool:
    # write your code here
    if len(robot1) != len(robot2):
        return False
    for i in robot1:
        if i == "serial_no":
            continue
        for k in robot2:
            if k == "serial_no":
                continue
            if i == k:
                if robot1[i] == robot2[i]:
                    continue
                else:
                    return False
            if i != k:
                continue
    return True

print(compare_robots(robot1, robot2))


def compare_robots(robot1: dict, robot2: dict) -> bool:
    # write your code here
    if len(robot1) != len(robot2):
        return False
    for i in robot1:
        if i == "serial_no":
            continue
        if i in robot1 and i in robot2:
            if robot1[i] == robot2[i]:
                continue
            else:
                return False
        else:
            return False
    return True

print(compare_robots(robot1, robot2))

"""

function compare_robots which takes two robots and returns True only if 
all characteristics of both robots match 
(property order is not important, only keys and values)
"""

# ##############################
# ###### Mentor resolution #####
# ##############################

def compare_robots(robot1: dict, robot2: dict) -> bool:
    for key in robot1:
        if key != "serial_no":
            if key not in robot2 or robot2[key] != robot1[key]:
                return False
    for key in robot2:
        if key != "serial_no":
            if key not in robot1 or robot2[key] != robot1[key]:
                return False
    return True

print(compare_robots(robot1, robot2))