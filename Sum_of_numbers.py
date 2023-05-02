first_number = 0
second_number = -1

def sum_of_numbers(first_number: int, second_number: int) -> int:
    
    if first_number < second_number:
        return sum(list(range(first_number, second_number + 1)))
    else:
        return sum(list(range(second_number, first_number + 1)))
    
print(sum_of_numbers(first_number, second_number))

#функцію sum_of_numbers, яка приймає два цілих числа first_number і second_number 
#(вони можуть бути як від'ємними, так і додатними) та 
#знаходить суму всіх цілих чисел між ними