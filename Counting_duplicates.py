def counting_duplicates(text: str) -> int:
    ls = []
    for i in set(text.upper()):
        ls.append(text.upper().count(i))
    
    proverca = all(x == 1 for x in ls)
    if proverca:
        return 0
                
    return len(ls) - ls.count(1)
        
print(counting_duplicates("aabBcde"))


### m ###

def counting_duplicates(text: str) -> int:
    count_of_duplicates = 0
    for char in set(text.lower()):
        if text.lower().count(char) > 1:
            count_of_duplicates += 1
    return count_of_duplicates
