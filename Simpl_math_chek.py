number = 


def check_number(number: int) -> list:
    # write your code here
    array =[] 
    if 0 >= number:
        array.append(False)
    else:
        array.append(True)

    if number % 2 == 0:
        array.append(True)
    else:
        array.append(False)

    if number % 10 == 0:
        array.append(True)
    else:
        array.append(False)
    return array

w = check_number(number)
print(w)

###### Mentor resolution #####
def check_number(number: int) -> list:
    return [number > 0, number % 2 == 0, number % 10 == 0]