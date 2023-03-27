row = [708, 3, 5, 116, 4, 9, 52, 60, 66, 123, 44, 5, 8]

def row_weights(row: list) -> list:
    # write your code here
    first_team = []
    for i in range(0, len(row), 2):
        first_team.append(row[i])
    return [sum(first_team), ((sum(row) - sum(first_team)))]

print(row_weights(row))

# ##############################
# ###### Mentor resolution #####
# ##############################

def row_weights(row: list) -> list:
    weights = [0, 0]
    for i, w in enumerate(row):
        weights[i % 2] += w
    return weights
print(row_weights(row))