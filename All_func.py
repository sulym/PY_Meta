def jaden_casing_strings(sentence: str) -> str:
    # write your code here
    
    a = sentence.split()
    b = [i.capitalize() for i in a ]
    return " ".join(b)


print(jaden_casing_strings("How can mirrors be real if our eyes aren't real"))

def product_of_maximum(num_list: list, number: int) -> int:
    sorted_numbers = sorted(num_list, reverse=True)
    max_numbers = sorted_numbers[:number]
    product = 1
    
    for num in max_numbers:
        product *= num
    
    return product


def sum_of_two_lowest(num_list: list) -> int:
    # write your code here
    sorted_num = sorted(num_list)
    return sorted_num[0] + sorted_num[1]
