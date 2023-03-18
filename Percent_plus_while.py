amount = 500
percent = 3
limit = 550
def get_years(amount: int, percent: int, limit: int) -> int:
    percent = (percent / 100)
    count = 0
    while limit > amount:
        amount += percent * amount
        if amount > limit:
            break
        count += 1
    return count

print(get_years(amount,percent,limit))

# ##############################
# ###### Mentor resolution #####
# ##############################

def get_years(amount: int, percent: int, limit: int) -> int:
    years = 0
    coefficient = 1 + percent / 100
    while amount * coefficient <= limit:
        amount *= coefficient
        years += 1
    return years