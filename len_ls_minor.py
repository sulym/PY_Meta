# def plus_one(digits: list[int]) -> list[int]:
#     # write your code here
#     a = "".join(str(num) for num in digits)
#     b = int(a) + 1
#     return [int(d) for d in str(b)]
# print(plus_one(digits=[1,2,3]))



# def intersection_of_two(nums1: list, nums2: list) -> list:
#     # write your code here
#     return sorted(set([i for i in nums1 for i in nums2 if i in nums1]))

# print(intersection_of_two(nums1=[1,5], nums2=[2,5]))

def roman_to_int(roman: str) -> int:
    # write your code here
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for c in roman[::-1]:
        value = roman_values[c]
        if value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value
    
    return result