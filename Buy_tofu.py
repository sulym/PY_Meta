def buy_tofu(cost: int, box: str) -> list or str:
    # write your code here
    
    box_ls = box.split()
    box_ls_new = [0, 0]
    for i in box_ls:
        if i == "mon":
            box_ls_new[0] += 1
        elif i == "monme":
            box_ls_new[1] += 1

    box_ls_new.append(box_ls_new[0] + (box_ls_new[1] * 60))

    coin_count = 0

    for coin in [1]:
        # Додаємо кількість монет даного номіналу до лічильника
        coin_count += cost // coin
        # Залишок суми, який треба досягти, оновлюємо на залишок після вирахування кількості монет даного номіналу
        cost %= coin

    box_ls_new.append(coin_count)


    a = cost // 60
    remaining_cost = cost % 60
    b = remaining_cost // 1
    
    # box_ls_new.append(a + b)

    if a > box_ls_new[1] and b > box_ls_new[1]:
        return "leaving the market"
    elif box_ls_new[2] < cost:
        return "leaving the market"
    elif box_ls_new[0] + box_ls_new[1] < box_ls_new[3]:
        return "leaving the market"
    

    return box_ls_new



print(buy_tofu(cost=124, box='mon mon mon mon mon apple mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon monme mon mon mon mon cloth mon mon mon mon mon mon mon mon mon cloth mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon'))