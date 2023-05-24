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