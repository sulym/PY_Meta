arry = [1,2,3,4,5]
arry_fals = [1,2,3,7,1]
arry_pust = []
arry_one = [42]

def is_sorted(box_numbers: list) -> bool:
    # write your code here
    for i in box_numbers:
        if len(box_numbers) == 0 or len(box_numbers) == 1:
            return True
        elif box_numbers == sorted(box_numbers):
            return True
        elif box_numbers != sorted(box_numbers):
            return False   
    return True

# Mentor resolution
#def is_sorted(box_numbers: list) -> bool:
    for i in range(len(box_numbers) - 1):
        if box_numbers[i] > box_numbers[i + 1]:
            return False
    return True