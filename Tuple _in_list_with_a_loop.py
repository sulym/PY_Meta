dino_names = ["Triceratops", "Saltopus"]
dino_lengths = [9, 1,]
dino_diets = ["carnivorous", "herbivorous"]


def create_dino_archive(
    dino_names: list,
    dino_lengths: list,
    dino_diets: list,
) -> list:
    # write your code here
    list_dino = []
    dino_in_tupl =[]
    for i in range(len(dino_names)):
        list_dino += [[dino_names[i]]]

    for k in range(len(dino_lengths)):
        list_dino[k] += [dino_lengths[k]]

    for j in range(len(dino_diets)):
        list_dino[j] += [dino_diets[j]]
        
    for m in range(len(list_dino)):
        dino_in_tupl.append(tuple(list_dino[m]))

    return dino_in_tupl
"""
Creating a list with a tuple through a loop
"""

# ##############################
# ###### Mentor resolution #####
# ##############################


def create_dino_archive(
    dino_names: list,
    dino_lengths: list,
    dino_diets: list,
) -> list:
    dinosaurs = []
    for i in range(len(dino_names)):
        dinosaurs.append((dino_names[i], dino_lengths[i], dino_diets[i]))
    return dinosaurs
        

        
    



print(create_dino_archive(dino_names,dino_lengths,dino_diets))