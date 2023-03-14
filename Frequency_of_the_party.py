quarantine_length = 3
frequency = 4

def count_networking(quarantine_length: int, frequency: int) -> int:
    # write your code here
    month = 12
    counter = 0
    for i in range(quarantine_length,month,frequency):
        counter +=1
    return counter

print(count_networking(quarantine_length,frequency))

""""Search for the frequency of the party depending on the conditions"""
# ##############################
# ###### Mentor resolution #####
# ##############################

def count_networking(quarantine_length: int, frequency: int) -> int:
    return (12 - quarantine_length + frequency - 1) // frequency