
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


def cycl(n):
    while True:
        n += -1
        if is_prime(n):
            return n
print(cycl(n=123))

#Finding a prime number less than a given number using a while loop

