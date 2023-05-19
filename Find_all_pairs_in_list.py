def find_all_pairs(num_list: list) -> int:
    # write your code here
    count = 0
    for i in set(num_list):
        count += num_list.count(i)// 2
    return count

print(find_all_pairs(num_list=[1, 2, 2, 20, 6, 20, 2, 6, 2]))