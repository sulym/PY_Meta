
users = [  { "name": "Emma", "status": "active", "country": "Ukraine" },
  { "name": "Avram", "status": "disabled", "country": "Poland" },
]

def remove_country(users: list) -> None:
    # write your code here
    for  i in range(len(users)):
        if "active" in users[i].values():
            users[i].pop("country")
    return users

print(remove_country(users))

"""
We delete information about the country from those users whose field "status" == "active"
and get a dictionary with the deleted country
"""
# ##############################
# ###### Mentor resolution #####
# ##############################

def remove_country(users: list) -> None:
    for user in users:
        if user["status"] == "active":
            del user["country"]


