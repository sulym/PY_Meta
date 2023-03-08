arry = [1,2,3,4,5]
arry_fals = [1,2,3,0,1]
arry_pust = []
arry_one = [42]

def is_sorted(box_numbers: list) -> bool:
    # write your code here
    for i in box_numbers:
        if len(box_numbers) == 0 or len(box_numbers) == 1:
            return True
      
    return True
        
        

w = is_sorted(arry)
print(w)