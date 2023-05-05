def sum_of_pairs(nums: list, sum_value: int) -> list:
    # write your code here
    for i in nums:
        for k in range(1, len(nums)):
            if i + nums[k] == sum_value:
                return [i, nums[k]]
    return None

#### M ####

def sum_of_pairs(nums: list, sum_value: int) -> list:
    for main_index in range(len(nums)):
        main_number = nums[main_index]
        
        for slave_index in range(main_index + 1, len(nums)):
            slave_number = nums[slave_index]
            if main_number + slave_number == sum_value:
                return [main_number, slave_number]
    return None

print(sum_of_pairs(nums=[4, 3, 2, 3, 4], sum_value=6))