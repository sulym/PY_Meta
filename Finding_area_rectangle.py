from typing import Union
side = 10
diagonal = 20

def get_rectangle_area(side: int, diagonal: int) -> Union[float, str]:
    # write your code here
    if side >= diagonal or side == 0:
        return "not a rectangle"
    second_side = abs((side ** 2) - (diagonal ** 2)) ** 0.5
    find_area = round((second_side * side), 1)
    return find_area

print(get_rectangle_area(side, diagonal))

### Finding the area of ​​a rectangle, knowing one side and the diagonal ###

######## Mentor resolution ########
import math
from typing import Union

#def get_rectangle_area(side: int, diagonal: int) -> Union[float, str]:
    if side >= diagonal or side <= 0 or diagonal <= 0:
        return "not a rectangle"
    other_side = math.sqrt(diagonal ** 2 - side ** 2)
    return round(side * other_side, 1)
