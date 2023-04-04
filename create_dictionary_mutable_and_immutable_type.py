ar = None
rs = True
cl = 1

def create_dictionary(*args) -> dict:
    typ_key_dict = {}
    for i in range(len(args)):
        if callable(args[i]):
            typ_key_dict[args[i]] = i
        elif args[i] is None:
            typ_key_dict[args[i]] = i
        elif isinstance(args[i], (int, float, str, bool, tuple, )):
            typ_key_dict[args[i]] = i
        else:
            print(f"Cannot add {args[i]} to the dict!")
    return typ_key_dict

print(create_dictionary(ar, rs, cl))

######## Mentor resolution ########

def create_dictionary(*args) -> dict:
    my_dict = {}
    for index, element in enumerate(args):
        if isinstance(element, (list, set, dict)):
            print(f"Cannot add {element} to the dict!")
        else:
            my_dict[element] = index
    return my_dict