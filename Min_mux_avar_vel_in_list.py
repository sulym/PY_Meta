# from math import floor
import math

test_results =[]
def get_speed_statistic(test_results: list) -> list:
    # write your code here
    array =[]
    
    if len(test_results) == 1:
         return test_results*3
    if test_results == 0:
         return test_results *3
    if len(test_results) == 0:
         return [0,0,0]
    
    counter = test_results[0]
    for i in range(len(test_results) - 1):
        if test_results[i+1] < counter:
            counter = test_results[i+1]
        array = [counter]
    a = 0
    for i in range(len(test_results) - 1):
        if test_results[i] < test_results[i+1]:
                a = test_results[i+1]
    array.append(a)
    b = 0
    for i in test_results:
        b += i       
    array.append(int( b / len(test_results))) # math.floor in line vs int
    return array

w = get_speed_statistic(test_results)
print(w)

############### my version is simplified ################

def get_speed_statistic(test_results: list) -> list:
    # write your code here
    array =[]
    
    if len(test_results) == 0:
         return test_results*3
    if test_results == 0:
         return test_results *3
    if len(test_results) == 0:
         return [0,0,0]

    array.append(min(test_results))
    array.append(max(test_results))
    array.append(floor(sum(test_results) / len(test_results)))

    return array

##### Mentor resolution #####
from math import floor

def get_speed_statistic(test_results: list) -> list:
    if len(test_results) == 0:
        return [0, 0, 0]
    min_element = test_results[0]
    max_element = test_results[0]
    sum_of_elements = 0
    for element in test_results:
        if element < min_element:
            min_element = element
        if element > max_element:
            max_element = element
        sum_of_elements += element
    return [
        min_element,
        max_element,
        floor(sum_of_elements / len(test_results)),
    ]