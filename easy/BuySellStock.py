from typing import List


class BuySellStock:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit

stock = BuySellStock()
prices = [7,6,5,4,3,2,0]
print(BuySellStock.maxProfit(stock, prices))