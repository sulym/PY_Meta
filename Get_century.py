
year = 2021
def get_century(year: int) -> int:
    # write your code here
    if year <= 100:
        return 1
    if year > 100:
        if year % 100 != 0:
                return year // 100 + 1
    return year // 100

print(get_century(year))

####Formula for finding the century (remainder of division and integer division)#####
##### Mentor resolution #####

#def get_century(year: int) -> int:
    if year == 0:
        return 1
    return (year + 99) // 100


