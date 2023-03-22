stones = "RRRRGGGGBBBB"

def color_stones(stones: str) -> int:
    # write your code here
    new_stone = ""
    for i in range(len(stones) - 1):
        if stones[i] != stones[i +1 ]:
            new_stone += stones[i]
    a = len(stones) - len(new_stone) - 1
    if a == -1:
        return 0
    return a

print(color_stones(stones))

"""
У Боба на столі лежать камені розміщені в ряд. 
Кожен з них може бути червоним, зеленим або синім та представлений символом R, G або B відповідно.
Допоможи Бобу знайти мінімальну кількість каменів, які він повинен прибрати зі столу, 
щоб після цього кожна пара каменів, що лежать поруч, містила камені різного кольору.
color_stones("RRRRGGGGBBBB") == 9 # "RRR", "GGG" та "BBB" потрібно прибрати;
в результаті залишиться "RGB"
"""

##############################
###### Mentor resolution #####
##############################

def color_stones(stones: str) -> int:
    count = 0
    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]:
            count += 1
    return count