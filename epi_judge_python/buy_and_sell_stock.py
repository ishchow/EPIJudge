from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    if not prices or len(prices) <= 1:
        return 0.0
    maxProfit = 0
    low, high, i = prices[0], 0, 1
    while i < len(prices):
        if prices[i] > low and prices[i] >= high:
            high = prices[i]
        else:
            maxProfit = max(maxProfit, high - low)
            low = prices[i]
            high = 0
        i += 1
    return maxProfit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
