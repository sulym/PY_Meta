import random
from typing import Generator


def dice_player(n_rounds: int) -> Generator[int, None, None]:
    for i in range(n_rounds):
        yield random.randint(1, 6)


def dice_game(n_rounds: int) -> str:
    # write your code here
    first = dice_player(n_rounds)
    second = dice_player(n_rounds)
    score_first = 0
    score_second = 0
    for i in range(n_rounds):
        score_1 = next(first)
        score_2 = next(second)
        print(score_1, score_2,)
        if score_1 > score_2:
            score_first += 1
        elif score_2 > score_1:
            score_second += 1
    if score_first > score_second:
        return "First"
    elif score_first < score_second:
        return "Second"
    
    return "Draw"

n_rounds = input("Введите количество раундов: ")
print(dice_game(int(n_rounds)))

