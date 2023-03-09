import math

current_production = 1000
month = 6
percent = 20
array = []

def get_plan(current_production: int, month: int, percent: int) -> list:
    array = []
    for i in range(month):
        current_production = current_production + math.floor(current_production / 100 * percent)
        array.append(math.floor(current_production))     
    return array

#### Mentor resolution ####
#def get_plan(current_production: int, month: int, percent: int) -> list:
    result_list = [current_production]
    for i in range(month):
        result_list.append(math.floor(result_list[-1] * (1 + percent / 100)))
    return result_list[1:]


    # # k = current_production / 100 * percent
    # array = [math.floor(k)+current_production]
    # t = array[0] / 100 * percent
    # array.append(math.floor(t)+array[0])
    # v = array[1] / 100 * percent
    # array.append(math.floor(v)+array[1])
    # a = array[2] / 100 * percent
    # array.append(math.floor(a)+array[2])
    


w = get_plan(current_production,month,percent)
print(w)