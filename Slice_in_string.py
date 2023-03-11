string = 'robot'

def split_string(string: str) -> list:
    # write your code here
    array_1 = []
    
    for i in range(len(string)):
        print(string[i:])
        print(string[:i])
        array_1 += [(string[i:] + string[:i]).upper()]
       
    return array_1

w = split_string(string)
print(w)

########  Mentor resolution #####

#def scrolling_text(string: str) -> list:
    string = string.upper()
    result_list = []
    for i in range(len(string)):
        result_list.append(string[i:] + string[:i])
    return result_list