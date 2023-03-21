boxes = "aabca"

def count_boxes(boxes: str) -> dict:
    # write your code here
    new_dict = {}
    for i in boxes:
        count = 0
        for k in boxes:
            if i == k:
                count += 1
        new_dict[i] = count
    return new_dict

print(count_boxes(boxes))

"""
Create a -count_boxes- function that accepts a string of -boxes-, 
where each character is the type of one of the -boxes- in the warehouse. 
Count how many boxes of each type are in stock and return the dictionary with the report.
"""
##############################
###### Mentor resolution #####
##############################

def count_boxes(boxes: str) -> dict:
    unique_boxes = set(boxes)
    dict_boxes = {}
    for box in unique_boxes:
        dict_boxes[box] = boxes.count(box)
    return dict_boxes

print(count_boxes(boxes))
