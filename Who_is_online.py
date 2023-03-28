friends = [{
  "username": "Alice",
  "status": "online",
  "lastActivity": 10
}, {
  "username": "Lucy",
  "status": "offline",
  "lastActivity": 22
}, {
  "username": "Bob",
  "status": "online",
  "lastActivity": 104
}]

def who_is_online(friends: list) -> dict:
    dict_online = {}
    online = []
    offline = []
    away = []
    for i in friends:
        if i.get("lastActivity") <= 10 and i.get("status") == "online":
            online.append(i.get("username"))
        elif i.get("lastActivity") > 10 and i.get("status") == "online":
            away.append(i.get("username"))
        elif i.get("status") == "offline":
            offline.append(i.get("username"))
    if online != []:
        dict_online["online"] = online
    if offline != []:
        dict_online["offline"] = offline
    if away != []:
        dict_online["away"] = away
    return dict_online
        
print(who_is_online(friends))

"""
Результат функції who_is_online:
{
  "online": ["Alice"],
  "offline": ["Lucy"],
  "away": ["Bob"]
}
"""

# ##############################
# ###### Mentor resolution #####
# ##############################

def who_is_online(friends: list) -> dict:
    result_dict = {}
    for friend in friends:
        username = friend["username"]
        group = "online"
        if friend["status"] == "online" and friend["lastActivity"] > 10:
            group = "away"
        elif friend["status"] == "offline":
            group = "offline"

        if group not in result_dict:
            result_dict[group] = [username]
        else:
            result_dict[group].append(username)
    return result_dict

print(who_is_online(friends))