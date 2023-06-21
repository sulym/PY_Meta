def create_dict(keys_tuple: tuple):
    # write your code here
    new_dict = {} 
    for index, velue in enumerate(keys_tuple):
        try:
            new_dict[velue] = index
        except TypeError:
            print(f"Cannot add {velue} to the dict!")
    return new_dict


print(create_dict(keys_tuple=(None, [1,2], 5)))