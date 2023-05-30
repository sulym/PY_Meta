def fibonacci_number(num_index: int) -> int:
    new = []
    a = 0
    b = 1
    for __ in range(num_index):
        a, b = b, a + b
        new.append(b)
    return new[num_index-1]
    
print(fibonacci_number(1))