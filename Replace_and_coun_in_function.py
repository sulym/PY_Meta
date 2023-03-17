text = 'dfadfdfa'
letter = "a"
#####Simple#####
def make_upper(text: str, letter: str) -> list:
    # write your code here
    new = text.replace(str(letter), letter.upper())
    counter = 0
    for i in range(len(text)):
        if text[i] == letter:
            counter += 1
    return [new, counter]

print(make_upper(text,letter))

""""
Iterating over the line with determination of the number of replaced characters
"""


def make_upper(text: str, letter: str) -> list:
#     # write your code here
    text_new = ""
    counter = 0
    for i in range(len(text)):
        if text[i] == letter:
            text_new += text[i].upper()
            counter =+1
            continue
        text_new += text[i]
    return [text_new,counter]

print(make_upper(text,letter))

##############################
###### Mentor resolution #####
##############################

def make_upper(text: str, letter: str) -> list:
    letter_count = text.count(letter)
    modified_text = text.replace(letter, letter.upper())
    return [modified_text, letter_count]