robots = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]
new_version = 10

def get_outdated(robots: list, new_version: int) -> list:
    # write your code here
    old_version_list = []
    for i in range(len(robots)):
        if robots[i].get("core_version") < new_version:
            old_version_list += [i]
    return old_version_list

print(get_outdated(robots, new_version))

"""
The -get_outdated- function takes a list of robots 
and returns a list of indexes of those robots whose -core_version- is less than -new_version-.
"""
##############################
###### Mentor resolution #####
##############################

def get_outdated(robots: list, new_version: int) -> list:
    outdated_robots = []
    for i, robot in enumerate(robots):
        if robot["core_version"] < new_version:
            outdated_robots.append(i)
    return outdated_robots