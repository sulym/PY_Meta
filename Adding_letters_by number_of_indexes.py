import timeit


def mumbling_v2(string: str) -> str:
    new_ls = []
    ls = []
    for i in range(len(string)):
        new_ls += [[string[i]]]
        for k in range(i):
            new_ls[i] += string[i]
    for i in new_ls:
        ls.append("".join(i).capitalize())
    return "-".join(ls)


### M ###

def mumbling_v1(word: str) -> str:
    new_word = ""
    for i in range(len(word)):
        new_word += (
            word[i].upper() + word[i].lower() * i + "-"
        )
    return new_word[:-1]

# Создаем строку для тестирования
test_str = 'testword1ghjkl;kjkl;\jkllllll'

# Тестируем первую функцию
t1 = timeit.timeit(lambda: mumbling_v1(test_str), number=10000)
print(f"mumbling_v1: {t1:.6f} seconds")

# Тестируем вторую функцию
t2 = timeit.timeit(lambda: mumbling_v2(test_str), number=10000)
print(f"mumbling_v2: {t2:.6f} seconds")