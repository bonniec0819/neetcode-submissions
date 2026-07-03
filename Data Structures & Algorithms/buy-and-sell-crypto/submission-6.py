class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = prices[0]
        for price in prices:
            if left > price:
                left = price
            profit = max(profit, price-left)
        return profit