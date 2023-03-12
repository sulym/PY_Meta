ls1 = [1,2,5]
ls2 = [3,6,1]

def combine_lists(ls1: list, ls2: list) -> list:
    # write your code here
    
    return [ls1[i] + ls2[i] for i in range (len(ls1))]

w = combine_lists(ls1,ls2)
print(w)

####Mentor resolution ####
#def combine_lists(ls1: list, ls2: list) -> list:
    result_list = []
    for i in range(len(ls1)):
        result_list.append(ls1[i] + ls2[i])
    return result_list