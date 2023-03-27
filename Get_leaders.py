numbers = [16, 17, 4, 3, 5, 2]

def get_leaders(numbers: list) -> list:
    # write your code here
    new_lider = []
    for i in range(len(numbers)):
        count = 0
        for k in range(i+1, len(numbers)):
            count += numbers[k]
        if numbers[i] > count:    
            new_lider.append(numbers[i])
    return new_lider

print(get_leaders(numbers))

"""
Функція get_leaders приймає список чисел, та повертає список Лідерів
Пояснення: Число вважається Лідером,
якщо воно більше за суму всіх елементів справа від нього
"""

##############################
###### Mentor resolution #####
##############################

def get_leaders(numbers: list) -> list:
    sum_of_last_elements = [0]
    for number in reversed(numbers):
        sum_of_last_elements.append(number + sum_of_last_elements[-1])
    sum_of_last_elements.reverse()
    leaders = []
    for i, number in enumerate(numbers):
        if number > sum_of_last_elements[i + 1]:
            leaders.append(number)
    return leaders