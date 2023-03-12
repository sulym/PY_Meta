ls1 = []
ls2 = []

def get_lists_sum(ls1: list, ls2: list) -> int:
    # write your code here
    count_1 = 0
    count_2 = 0
    for i in ls1:
        count_1 += i
    for i in ls2:
        count_2 += i
    return count_1 + count_2

w = get_lists_sum(ls1,ls2)
print(w)

###### Mentor resolution ####

#def get_lists_sum(ls1: list, ls2: list) -> int:
    sum_of_elements = 0
    for element in ls1:
        sum_of_elements += element
    for element in ls2:
        sum_of_elements += element
    return sum_of_elements