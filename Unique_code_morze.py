# def longest_gap(num_decimal: int) -> int:
#     a = str(bin(num_decimal)[2:])
#     print(a)
#     x =  a.split("1")
#     leen = 0
#     for i in range(len(x)-1):
#         if len(x[i]) > leen and x[i+ 1] != 0:
#             leen = len(x[i])
#     return leen
# print(longest_gap(2))


# def printer_errors(printer_label: str) -> str:
#     # write your code here
#     a = 0
#     ls = list("nopqrstuvwxyz")
#     for i in printer_label:
#         if i in ls:
#             a += 1
#     return f'"{a}/{len(printer_label)}"'




# print(printer_errors("abcdxyz"))


morze_dict = {"a": ".-",
"b": "-...",
"c": "-.-.",
"d": "-..",
"e": ".",
"f": "..-.",
"g": "--.",
"h": "....",
"i": "..",
"j": ".---",
"k": "-.-",
"l": ".-..",
"m": "--",
"n": "-.",
"o": "---",
"p": ".--.",
"q": "--.-",
"r": ".-.",
"s": "...",
"t": "-",
"u": "..-",
"v": "...-",
"w": ".--",
"x": "-..-",
"y": "-.--",
"z": "--.."}

def unique_code(words: list) -> int:
    # write your code here
    new_ls_morze = []
    for i in words:
        morze_simbl = ""
        for k in i:
            morze_simbl += morze_dict[k]
        new_ls_morze.append(morze_simbl)
    count = 1
    for i in range(len(new_ls_morze) - 1):
        if new_ls_morze[i] == new_ls_morze[i + 1]:
            continue
        count += 1
    return count



uni = ["gin", "zen"]

print(unique_code(uni))