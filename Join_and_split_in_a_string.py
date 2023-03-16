words = "my favorite variable name is x"
number_of_words = 2

def make_variable_name(words: str, number_of_words: int) -> str:
    # write your code here
    words = words.split()
    words_new = []
    for i in range(0,number_of_words):
        words_new += [words[i]]
    return " ".join(words_new)

print(make_variable_name(words,number_of_words))

""""Using a function to split a string into a given number of words for a variable."""
##############################
###### Mentor resolution #####
##############################

def make_variable_name(words: str, number_of_words: int) -> str:
    return "_".join(words.split(" ")[:number_of_words])
