"""
У тебе є список, де кожен елемент – ціна акції в окремо взятий день.

Тобі потрібно максимізувати свій прибуток, обравши один день для покупки акції та обравши інший день у майбутньому,
щоб цю акцію продати.

Напиши функцію buy_and_sell_stock, яка повертає максимальний прибуток, 
який можна отримати від угоди. Якщо ти не можеш отримати прибуток, то поверни 0.

"""


def buy_and_sell_stock(prices: list) -> int:
    # write your code here
    for i in range(len(prices)):
        if max(prices[i:]) - prices[i] > 0 and \
        ((prices[i] <= min(prices[i:]) or (min(prices[i:]) < prices[i]))):
            return max(prices[i:]) - prices[i]
    return 0

print(buy_and_sell_stock([21, 56, 52, 76, 22, 11]))

### M ###

def buy_and_sell_stock(prices: list) -> int:
    left = 0  # Buy
    right = 1  # Sell
    max_profit = 0
    while right < len(prices):
        current_profit = prices[right] - prices[left]  # our current Profit
        if prices[left] < prices[right]:
            max_profit = max(current_profit, max_profit)
        else:
            left = right
        right += 1
    return max_profit


### GPT ###

def buy_and_sell_stock(prices: list) -> int:
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print(buy_and_sell_stock([21, 56, 52, 76, 22, 11]))


def buy_and_sell_stock(prices):
    if len(prices) < 2:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    
    return max_profit