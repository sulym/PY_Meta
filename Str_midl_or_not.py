def middle_character(word: str) -> str:
    # write your code here
    if len(word) % 2 != 0:
        return word[int(len(word) / 2)]
    return word[round(len(word) / 2) - 1] + word[int((len(word) / 2))]

print(middle_character(word="tnt4"))