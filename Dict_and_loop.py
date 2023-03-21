users = [
  {
    "last_name": "Holy",
    "full_name": "Jack Holy",
  },
  {
    "last_name": "Adams",
    "full_name": "Mike Adams",
  },
]

def restore_names(users: list) -> None:
    # write your code here
    new_dict = {}
    for i in range(len(users)):
        for k, v in users[i].items():
            if k == "full_name":
                a = v.partition(' ')[0]
                new_dict["first_name"] = a
        users[i].update(new_dict)
    return users

print(restore_names(users))


""""
Adding a new value to the dictionary with a search through the for cycle,
and combining two dictionaries with the update function
"""
# ##############################
# ###### Mentor resolution #####
# ##############################



def restore_names(users: list) -> None:
    for user in users:
        if "first_name" not in user:
            user["first_name"] = user["full_name"].split(" ")[0]