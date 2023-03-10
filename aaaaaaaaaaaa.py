import math

test_results =[1,2,3,4,5,6,8,6]
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
    array.append(math.floor(sum(test_results) / len(test_results)))

    return array
w = get_speed_statistic(test_results)
print(w)