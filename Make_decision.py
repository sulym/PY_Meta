fuel_remaining = int(1)
distance = int(15)
fuel_consumption = float(9)

def make_decision(
    fuel_remaining: int,
    distance: int,
    fuel_consumption: float
) -> str:
    # write your code here
    if fuel_remaining == 0:
        return "ask for help"
    if fuel_remaining < 0 or distance < 0 or fuel_consumption <= 0:
        return "please, enter the valid data"
    if ((100 / fuel_consumption) * fuel_remaining) >= distance:
        return "reach gas station by themselves"
    return "ask for help"

print(make_decision(fuel_remaining,distance,fuel_consumption))

##############################
###### Mentor resolution #####
##############################

def make_decision(
    fuel_remaining: int,
    distance: int,
    fuel_consumption: float
) -> str:
    if fuel_remaining < 0 or distance < 0 or fuel_consumption <= 0:
        return "please, enter the valid data"
    return (
        "reach gas station by themselves"
        if fuel_remaining >= distance * fuel_consumption / 100
        else "ask for help"
    )
