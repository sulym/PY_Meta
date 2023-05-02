long_date = "Wed September 1, 3am"

def shorten_to_date(long_date: str) -> str:
    # write your code here
    return "".join(long_date.split(",")[0])

print(shorten_to_date(long_date))

### Скорочення рядка
