import random

""""The function outputs a list with random numbers, 
---randint--- difference can only be used when you know both intervals,
---randrange--- knowing only one interval and it will work"""

min_value = 0
max_value = 1
length = 5

def generate_random_list(min_value: int, max_value: int, length: int) -> list:
    # write your code here
    list_number = []
    for i in range(length):
        list_number.append(random.randrange(min_value,max_value+1))
    return list_number

print(generate_random_list(min_value, max_value, length))


##############################
###### Mentor resolution #####
##############################

def generate_random_list(min_value: int, max_value: int, length: int) -> list:
    random_list = []
    for _ in range(length):
        random_list.append(random.randint(min_value, max_value))
    return random_list