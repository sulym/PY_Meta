
def convert_to_title(n: int) -> str:
    result = ""
    while n > 0:
        n -= 1
        remainder = n % 26
        result = chr(ord('A') + remainder) + result
        n //= 26
    return result


print(convert_to_title(n=23))


#### M ####

def convert_to_title(num: int) -> str:
    capitals = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
    result = []
    while num > 0:
        result.append(capitals[(num - 1) % 26])
        num = (num - 1) // 26
    result.reverse()
    return "".join(result)

