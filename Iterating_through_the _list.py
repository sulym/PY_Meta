# def get_location(coordinates: list, commands: list) -> list:
    # write your code here
coordinates = [4,3]
commands = ['left','back', 'back', 'forward']
def get_location(coordinates: list, commands: list) -> list:
    
    for u in commands:
        if u == "left":
            coordinates[0] -= 1
        elif u == "right":
            coordinates[0] += 1
        elif u == "back" :
            coordinates[1] -= 1
        else:
            u == "forward"
            coordinates[1] += 1
    return coordinates
w = get_location(coordinates,commands)
print(w)