class_register = {
  "Robb Stark": 10,
  "Sansa Stark": 12,
  "Arya Stark": 6,
  "Bran Stark": 8,
  "Jon Snow": 8,
}

def count_marks(class_register: dict) -> dict:
    # write your code here
    unique_class = sorted(set(class_register.values()))
    unique_class_numbers = class_register.values()
    dict_new = {}
    for i in unique_class:
        count = 0
        for k in unique_class_numbers:
            if i == k:
                count += 1
        dict_new[i] = count
    return dict_new

print(count_marks(class_register))

"""
Write the count_marks function, which has one parameter - the school journal class_register 
and returns the desired statistics. The journal is stored in the form of a dictionary, 
where the keys are the names of students, and the values are grades.
"""

# ##############################
# ###### Mentor resolution #####
# ##############################

def count_marks(class_register: dict) -> dict:
    marks_count = {}
    for mark in class_register.values():
        if mark not in marks_count:
            marks_count[mark] = 1
        else:
            marks_count[mark] += 1
    return marks_count


print(count_marks(class_register))