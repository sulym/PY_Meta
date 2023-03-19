def detect_lowercase_words() -> None:
    # write your code here
    while True:
        word = str(input())
        if word == "exit":
            break
        counter_words = 0
        for i in word:
            if i == i.upper():
                counter_words += 1
                break
        if counter_words == 0:
            print(f"{word} detected")

detect_lowercase_words()

"""
The input function with a while loop

Write a function detect_lowercase_words
That reads one line at a time using the input function 
and checks whether the word has no uppercase letters.
If not, it displays the line {word} detected, where word is the word entered by the user.
The function works until it reads the word exit.
"""
# ##############################
# ###### Mentor resolution #####
# ##############################

def detect_lowercase_words() -> None:
    while True:
        word = input()
        if word == "exit":
            break
        if word.lower() == word:
            print(f"{word} detected")
