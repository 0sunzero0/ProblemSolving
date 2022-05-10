def maxProfit(prices):
    min_price = 10 * 10 * 10 * 10
    profit = 0

    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)

    return profit
