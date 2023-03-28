string = "arithmetics"

def count_letters_in_string(string: str) -> dict:
    # write your code here
    new_str_dic = {}
    for i in string:
        new_str_dic[i] = string.count(i)
    return new_str_dic

print(count_letters_in_string(string))

##############################
###### Mentor resolution #####
##############################

def count_letters_in_string(string: str) -> dict:
    letters_count = {}
    for letter in string:
        if letter not in letters_count:
            letters_count[letter] = 1
        else:
            letters_count[letter] += 1
    return letters_count