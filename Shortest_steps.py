goal_num = 7


def shortest_step(n):
    steps = 0  # змінна, що зберігає кількість кроків
    while n > 1:  # виконуємо поки n більше 1
        if n % 2 == 0:  # якщо n парне
            n //= 2  # ділимо n на 2
        else:
            n -= 1  # інакше віднімаємо 1
        steps += 1  # збільшуємо кількість кроків
    return steps  # повертаємо кількість кроків


print(shortest_step(goal_num))