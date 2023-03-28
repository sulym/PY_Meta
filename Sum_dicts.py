first = {"a": 2, "b": 4 }
second = {"a": 2, "b": 10}
third = {"d": -5}
"""
Реалізуй функцію sum_dicts,
яка приймає необмежену кількість словників та повертає словник, який об'єднує їх.
"""

def sum_dicts(*args) -> dict:
    # write your code here
    new_dict = {}
    print(len(args))
    for i in args:
        for k in i:
            if k not in new_dict:
                new_dict[k] = i[k]
            else:
                new_dict[k] += i[k]
    return new_dict

print(sum_dicts(first, second))