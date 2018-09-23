from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    if not prices or len(prices) <= 1:
        return 0.0
    minPrice, maxProfit = float('inf'), 0
    for p in prices:
        maxProfit = max(maxProfit, p - minPrice)
        minPrice = min(minPrice, p)
    return maxProfit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
