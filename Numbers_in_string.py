from typing import Union

guests_input = "dsfsdf 7 or 9"


def calculate_guests(guests_input: str) -> Union[int, str]:
    # write your code here
    number = ""
    if guests_input == "0" or guests_input == "":
        return "not a number"
    for i in range(len(guests_input)-1):
        if guests_input[i].isdigit():
            number += guests_input[i]
            if guests_input[i+1].isdigit():
                number += guests_input[i+1]
            return int(number)
    if number == "":
        for i in guests_input:
            if i.isdigit():
                number += i
                return int(number)
    return "not a number"


print(calculate_guests(guests_input))

""""
Using the --.isdigit-- and mentor --isnumeric-- function,
checking an element for a number
"""

##############################
###### Mentor resolution #####
##############################

from typing import Union


def calculate_guests(guests_input: str) -> Union[int, str]:
    number_str = ""
    for char in guests_input:
        if char.isnumeric():
            number_str += char
        elif len(number_str) != 0:
            break
    return (
        int(number_str)
        if len(number_str) > 0 and int(number_str) != 0
        else "not a number"
    )