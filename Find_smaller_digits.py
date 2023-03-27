ls = [5, 4, 3, 2, 1]
def find_smaller_digits(ls: list) -> list:
    # write your code here
    result_list = []
    a = 0
    for i in range(len(ls)):
        count = 0
        for k in range(i+1, len(ls)):
            if ls[i] > ls[k]:
                count += 1
        result_list.append(count)
    return result_list
    
print(find_smaller_digits(ls))

"""
Напишіть функцію find_smaller_digits(ls), яка приймає список чисел ls
та повертає новий список чисел result_list.
Кожне число нового списку result_list[i] - це кількість чисел праворуч від ls[i], 
які менші за ls[i]
"""

##############################
###### Mentor resolution #####
##############################

def find_smaller_digits(ls: list) -> list:
    result_list = []
    for i in range(len(ls)):
        result_list.append(0)
        for j in range(i + 1, len(ls)):
            if ls[i] > ls[j]:
                result_list[-1] += 1
    return result_list

print(find_smaller_digits(ls))