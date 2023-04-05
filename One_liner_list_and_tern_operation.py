numbers = [145, -24442, 317]



def even_odd(numbers: list) -> list:
    # write your code here
    return ['even' if num % 2 == 0 else "odd" for num in numbers] 




print(even_odd(numbers))