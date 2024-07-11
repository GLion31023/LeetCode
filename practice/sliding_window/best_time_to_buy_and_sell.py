def max_profit(prices: list[int]) -> int:
    profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        profit = max(profit, price - min_price)
        min_price = min(min_price, price)

    return profit


print(max_profit([10, 1, 5, 6, 7, 1]))
print(max_profit([10, 8, 7, 5, 2]))
print(max_profit([5, 1, 5, 6, 7, 1, 10]))
print(max_profit([2, 1, 2, 1, 0, 1, 2]))
