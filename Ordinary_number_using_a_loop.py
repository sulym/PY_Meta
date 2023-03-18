number = 10000
def check_is_prime(number: int) -> bool:
    # write your code here
    i = 2
    count = 0
    while i <= number:
        if number % i == 0:
            count += 1
        i += 1
    if count == 1:
        return True
    return False

print(check_is_prime(number))

"""
Determining an ordinary number using a loop
A number is prime if it is natural and has exactly two distinct divisors: 1 and itself.
"""
# ##############################
# ###### Mentor resolution #####
# ##############################

def check_is_prime(number: int) -> bool:
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        print(int(number ** 0.5))
        if number % i == 0:
            print(number % i)
            return False
    return True

print(check_is_prime(number))