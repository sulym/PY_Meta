# def fibonacci_generator():
#     # write your code here
#     a = 0,
#     b = 1,
#     a,b = 

def fibonacci_generator(n: int) -> int:
    # write your code here
    a = 0
    b = 1
    for __ in range(n):
        yield a
        a, b = b, a + b
        



fib = fibonacci_generator(4)
print(next(fib))
print(next(fib))