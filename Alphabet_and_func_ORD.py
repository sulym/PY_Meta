letters = "abd"
def is_alphabet(letters: str) -> bool:
    # write your code here
    letters = letters.lower()
    for i in range(len(letters) - 1):
        if letters[i] >= letters[i + 1]:
            return False
    if ord(letters[len(letters) - 2]) + 1 < ord(letters[len(letters) - 1]):
        return False
    return True

print(is_alphabet(letters))

""""In the code above, we used the --ord()-- function 
to convert a character to an integer, i.e. an ASCII value."""
##############################
###### Mentor resolution #####
##############################

def is_alphabet(letters: str) -> bool:
    letters = letters.lower()
    for i in range(len(letters) - 1):
        if ord(letters[i + 1]) - ord(letters[i]) != 1:
            return False
    return True