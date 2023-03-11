string = ' '

def split_string(string: str) -> list:
    # write your code here
    array_1 = []
    counter = []
    if string == '':
        return array_1
    elif string == ' ':
        return [' _']
    
    for i in range (0, len(string),2):
        counter = string[i:i+2]
        if len(counter) == 1:
            counter += '_'
        array_1.append(counter)
    return array_1

##### Mentor resolution ####
    def split_string(string: str) -> list:
    if len(string) % 2 == 1:
        string += "_"
    result_list = []
    for i in range(len(string) // 2):
        result_list.append(string[i * 2 : (i + 1) * 2])
    return result_list


# array = [string[i:i+n] for i in range(0, len(string), n)]
# An example of a loop in one line in a list





    
w = split_string(string)
print(w)