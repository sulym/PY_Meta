colors = [2, 2, 2, 2, 2]

def count_matching_socks(colors: list) -> int:
    new_list_socks = {}
    count_pair = 0
    for i in colors:
        if i not in new_list_socks:
            new_list_socks[i] = 1
        elif i in new_list_socks:
            new_list_socks[i] += 1

    for k in new_list_socks:
        if new_list_socks[k] // 2 != 0:
            count_pair += new_list_socks[k] // 2
    return count_pair

print(count_matching_socks(colors))

"""
count_matching_socks яка приймає массив чисел colors, 
де кожне число — певного кольору,
та повертає максимальну кількість пар (два однакових числа)
# [10, 10] - одна пара шкарпеток кольору 10.
# [2, 2, 2, 2, 2] - дві пари шкарпеток кольору 2.
# [10, 20, 30, 40, 50, 60] - всі шкарпетки різних кольорів - 0 пар.
# [10, 20, 30, 10, 20, 60] - 2 пари. Одна кольору 10 та одна кольору 20.
"""

def count_matching_socks(colors: list) -> int:
    count_of_colors = {}
    for color in colors:
        if color not in count_of_colors:
            count_of_colors[color] = 1
        else:
            count_of_colors[color] += 1
    pairs = 0
    for color in count_of_colors:
        pairs += count_of_colors[color] // 2
    return pairs

print(count_matching_socks(colors))