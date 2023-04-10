# first = [True, 3, 9, 11, 15]
# second = [True, 3, 11]

# def list_comparator(first: list, second: list) -> int:
#     # write your code here
#     count = 0
#     for one in first:
#         if one in second:
#             count += 1
#     return count
# print(list_comparator(first, second))


# def is_leap_year(year: int) -> bool:
#     # write your code here
#     if year % 4 and year % 400:
#         return True
#     else:
#         return False
# print(is_leap_year(1234))



# def rotate_list(nums: list, steps: int) -> list:
#     # write your code here
#     return nums[-steps:] + nums[:-steps]
# print(rotate_list(nums=[1, 2, 3, 4, 5, 6, 7], steps = 3))

# def odd_ones_out(numbers: list) -> list:
#     # write your code here
#     new_num_ls = []
#     for num in numbers:
#         if numbers.count(num) % 2 == 0:
#             new_num_ls.append(num)
#         else:
#             continue
#     return new_num_ls

# def odd_ones_out(numbers: list) -> list:
#     return [num for num in numbers if numbers.count(num) % 2 == 0 ]

# print(odd_ones_out([26, 23, 24, 17, 23, 24, 23, 26]))


# def coin_combination(cents: int) -> list:
#     # write your code here
#     new_ls_coin = [0, 0, 0, 0]
#     new_ls_coin[3] = cents // 25
#     new_ls_coin[2] = (cents - (new_ls_coin[3]*25)) // 10
#     new_ls_coin[1] = (cents - (new_ls_coin[3]*25 + new_ls_coin[2]*10)) // 5
#     new_ls_coin[0] = (cents - (new_ls_coin[3]*25 + new_ls_coin[2]*10 + new_ls_coin[1]*5)) // 1
#     return new_ls_coin

# print(coin_combination(1))

# first_string="xyaabbbccccdefww"
# second_string="xxxxyyyyabklmopq"
# def two_to_one(first_str: str, second_str: str) -> str:
#     # write your code here
#     my_ls = first_str.split() + second_str.split()
#     my_ls = "".join(my_ls)
#     return "".join(sorted(set(my_ls)))

# print(two_to_one(first_string, second_string))


# def detect_capital(word: str) -> bool:
#     # write your code here
#     return all(st == st.upper() for st in word) or all(st == st.lower() for st in word) or word == word.capitalize()
        

# print(detect_capital(word="Qwerty"))


# def rgb_to_hex(r: int, g: int, b: int) -> str:
#     # write your code here
#     my_ls = [r, g, b]
#     for num in range(len(my_ls)):
#         if my_ls[num] <= 0:
#             my_ls[num] = "00"
#         elif my_ls[num] > 255:
#             my_ls[num] = "FF"
#         else:
#             my_ls[num] = hex(my_ls[num]).strip("0x").upper()
#     print(my_ls)
#     return "".join(my_ls)

# print(rgb_to_hex(1,2,3))



def capitals_first(sentence: str) -> str:
    # write your code here
    new_sentance = sentence.split()
    new_sent = [new for new in new_sentance if new == new.upper() or new == new.capitalize()]
    last = new_sent + [i for i in new_sentance if i == i.lower()]
    return " ".join(last)

print(capitals_first("z x c b Z Z X CC B") )