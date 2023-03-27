numbers = [1, 5, 2]

def product_list(numbers: list) -> list:
    # write your code here
    new_number_list = []
    for i in range(len(numbers)):
        new_ls = numbers.copy()
        del new_ls[i]
        count = 1
        for k in new_ls:
            count *= k
        new_number_list.append(count)
    return new_number_list

print(product_list(numbers))
"""
product_list, яка отримує список чисел numbers та повертає список такого ж розміру, 
де кожен елемент дорівнює добутку усіх елементів списку справа та зліва від цього елемента.
"""

# ##############################
# ###### Mentor resolution #####
# ##############################

def product_list(numbers: list) -> list:
    product_of_all_elements = 1
    for number in numbers:
        product_of_all_elements *= number
    return [product_of_all_elements // number for number in numbers]

print(product_list(numbers))