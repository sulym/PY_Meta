import math

number = 1
def number_checker(number: float) -> list:
    # write your code here
    if number == 0:
        return [True, False]
    if math.isinf(number):
        return [True, False]
    if math.isnan(number):
        return [False, True]
    return [False, False]

print(number_checker(number))

"""Formula for finding infinity and value "nan" and writing to a list"""
# math.isinf(number)
# math.isnan(number)

##### Mentor resolution #####

#def number_checker(number: float) -> list:
    return [math.isinf(number), not (number == number)]
