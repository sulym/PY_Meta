number = 123

def is_jumping(number: int) -> str:
    # write your code here
    number = str(number)
    for i in range(len(number)-1):
        if int(number[i+1]) == int(number[i]):
            return 'NOT JUMPING'
    for i in range(len(number)-1):
        if int(number[i+1]) > int(number[i]) +1 or int(number[i]) > int((number[i+1]))+1 \
        and int(number[i]) == int(number[i]):
            return 'NOT JUMPING'
    return "JUMPING"
print(is_jumping(number))

"""is_jumping, яка приймає число та повертає рядок "JUMPING",
# якщо кожна цифра в числі відрізняється від сусідньої на 1, 
# а якщо ні — рядок "NOT JUMPING"."""

#### Mentor resolution ####
#def is_jumping(number: int) -> str:
    prev_digit = number % 10
    number //= 10
    while number > 0:
        a = abs(prev_digit - number % 10)
        print(a)
        if a != 1:
            return "NOT JUMPING"
        prev_digit = number % 10
        number //= 10
    return "JUMPING"

print(is_jumping(number))