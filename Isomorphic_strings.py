first_string= "paper"
second_string= "pancil"

"""
Напиши функцію isomorphic_strings, яка приймає рядки first_string, second_string та визначає, чи вони є ізоморфними.
Рядки ізоморфні, якщо кількість та розташування символів в first_string є пропорційними до кількості та розташування в second_string.
Усі входження конкретних символів мають бути замінені іншими символами зі збереженням їхнього порядку.
"""

def isomorphic_strings(first_string, second_string):
    # перевіряємо, чи мають рядки однакову довжину
    if len(first_string) != len(second_string):
        return False
    
    # створюємо словник, який буде зберігати відповідність між символами рядків
    mapping = {}
    
    # перевіряємо, чи відповідає кожен символ першого рядка символу другого рядка
    for i in range(len(first_string)):
        if first_string[i] not in mapping:
            # якщо символ першого рядка ще не зустрічався,
            # перевіряємо, чи символ другого рядка вже має відповідність
            if second_string[i] in mapping.values():
                # якщо символ другого рядка має вже відповідність, то рядки не є ізоморфними
                return False
            # якщо символ другого рядка ще не має відповідності,
            # додаємо відповідність для цих символів
            mapping[first_string[i]] = second_string[i]
        else:
            # якщо символ першого рядка вже зустрічався,
            # перевіряємо, чи символ другого рядка відповідає йому
            if mapping[first_string[i]] != second_string[i]:
                # якщо символ другого рядка не відповідає символу першого рядка, то рядки не є ізоморфними
                return False
    
    # якщо всі символи першого рядка мають відповідні символи у другому рядку,
    # і навпаки, то рядки є ізоморфними
    return True


#### M ####

def isomorphic_strings(first_string: str, second_string: str) -> bool:
    d1, d2 = {}, {}
    for i, val in enumerate(first_string):
        d1[val] = d1.get(val, []) + [i]
    for i, val in enumerate(second_string):
        d2[val] = d2.get(val, []) + [i]
    return sorted(d1.values()) == sorted(d2.values())

print(isomorphic_strings(first_string, second_string))
