def buy_tofu(cost: int, box: str) -> list or str:
    num_monme_coins = box.count("monme")
    num_mon_coins = box.count("mon") - num_monme_coins
    sum_coins = num_monme_coins * 60 + num_mon_coins
    pay_monme = min(cost // 60, num_monme_coins)
    remain = cost - 60 * pay_monme
    if remain > num_mon_coins:
        return "leaving the market"
    return [num_mon_coins, num_monme_coins, sum_coins, pay_monme + remain]