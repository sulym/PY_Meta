sentence = "Delete all vowels!"

def disemvowel_trolls(sentence: str) -> str:
    # write your code here
    abs = ["A", "E", "I", "O", "U"]
    new_str = sentence
    for i in sentence:
        if i.upper() in abs:
            new_str = new_str.replace(i, "")
    return new_str

print(disemvowel_trolls(sentence))



order = "cokeonionringsfriesfpizzachickenmilkshakesandwichburger"

def get_order(order: str) -> str:
    # write your code here
    arr = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    
    ls = ["burger", "fries", "chicken", "pizza", "sandwich", "onionrings", "milkshake", "coke"]
    strin_name = ""
    new_order = []
    for i in order:
        strin_name += i
        if strin_name == "fpizza":
            strin_name = "pizza"
        if strin_name in ls:
            new_order.append(strin_name.capitalize())
            strin_name = ""
    new_order_new = []
    for i in arr:
        if i in new_order:
            war = new_order.count(i)
            for k in range(war):
                new_order_new.append(i)
    return " ".join(new_order_new)
print(get_order(order))

def get_order(order: str) -> str:
    menu = [
        "burger",
        "fries",
        "chicken",
        "pizza",
        "sandwich",
        "onionrings",
        "milkshake",
        "coke",
    ]
    clean_order = ""
    for meal in menu:
        clean_order += (meal.capitalize() + " ") * order.count(meal)
    return clean_order
print(get_order(order))

word = "MATE academy 2022 @)@@"

def fix_string_case(word: str) -> str:
    # write your code here
    count_1 = 0
    count_2 = 0
    for i in word:
        if i == i.upper() and i != " " and i != "@":
            count_1 += 1
        else:
            count_2 += 1
    if count_1 > count_2:
        return word.upper()
    else:
        return word.lower()

print(fix_string_case(word))

def fix_string_case(word: str) -> str:
    lower_count = 0
    upper_count = 0
    for i in range(len(word)):
        if word[i].islower():
            lower_count += 1
        elif word[i].isupper():
            upper_count += 1
    if lower_count < upper_count:
        return word.upper()
    return word.lower()

string = "b"
rank = 2

def square_color(string: str, rank: int) -> str:
    # write your code here
    arr_1 = ["a", "c", "e", "g"]
    arr_2 = ["b", "d", "f", "h"]
    if string in arr_1:
        if rank % 2 == 0:
            return "white"
        else:
            return "black"
    elif string in arr_2:
        if rank % 2 == 0:
            return "black"
        else:
            return "white"

print(square_color(string, rank))


nums = [3, 2, 4]
target = 6
def two_sum(nums: list, target: int) -> list:
    # write your code here
    for i in range(len(nums)):
        for k in range(len(nums)-1, 0, -1):
            if nums[i] + nums[k] == target:
                return [i, k]


print(two_sum(nums, target))

jewels = "z"
stones = "aAAbbbbZZ"
def jewels_and_stones(jewels: str, stones: str) -> int:
    # write your code here
    count_all = 0
    for i in jewels:
        count_all += stones.count(i)
    return count_all
print(jewels_and_stones(jewels,stones))

lst = []

def partlist(lst: list) -> list:
    # write your code here
    pass


print(partlist(lst))

partlist(["I", "wish", "I"])  # повертає [("I", "wish I"), ("I wish", "I")]
partlist(["I", "wish", "I", "hadn't"])  # повертає [("I", "wish I hadn't"), ("I wish", "I hadn't"), ("I wish I", "hadn't")]
