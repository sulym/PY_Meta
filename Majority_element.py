nums = [0,0,0,34,55]

def majority_element(nums: list) -> int:
    # write your code here
    c = len(nums) / 2
    b = [item for item in set(nums) if nums.count(item) > c]
    return b[0]

print(majority_element(nums))