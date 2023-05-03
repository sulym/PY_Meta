def get_section_id(scroll: int, sizes: list) -> int:
    # write your code here
    count_valeu = 0
    for index, value in enumerate(sizes):
        count_valeu += value  - 1
        if scroll > count_valeu:
            continue
        elif scroll <= count_valeu:
            return index
    return -1

print(get_section_id(scroll=1600, sizes=[300,200,400,600,100]))

#### M ####

def get_section_id(scroll: int, sizes: list) -> int:
    counter = 0
    for index, size in enumerate(sizes):
        counter += size
        if scroll < counter: return index
    return -1