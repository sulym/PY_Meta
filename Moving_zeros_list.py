nums = [0,0]

def moving_zeros(nums: list) -> list:
    a = nums.count(0)
    return [i for i in nums if i != 0] + ([0] * a)

### M ###

def moving_zeros(nums: list) -> list:
    new_lst = []
    zero_lst = []
    for item in nums:
        if item != 0:
            new_lst.append(item)
        else:
            zero_lst.append(item)
    new_lst.extend(zero_lst)
    return new_lst