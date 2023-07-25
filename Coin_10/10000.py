# import random

# def flip_coin(num_experiments=10000, num_flips=11):
#     results = {}

#     for _ in range(num_experiments):
#         heads_count = 0
#         for _ in range(num_flips):
#             coin_flip = random.randint(0, 1)
#             if coin_flip == 1:
#                 heads_count += 1

#         if heads_count in results:
#             results[heads_count] += 1
#         else:
#             results[heads_count] = 1
    
#     total_experiments = num_experiments
#     percentages = {heads: (count / total_experiments) * 100 for heads, count in results.items()}

#     final_dict = {}
#     for heads, percentage in percentages.items():
#         final_dict[heads] = round(percentage, 2)
    
#     return sorted(final_dict.items(), key=lambda item: item[0])
# print(flip_coin())



import random


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        num_heads = sum(random.randint(0, 1) for _ in range(10))
        results[num_heads] += 1

    for key in results:
        results[key] = round((results[key] / num_cases) * 100, 2)

    return results

print(flip_coin())