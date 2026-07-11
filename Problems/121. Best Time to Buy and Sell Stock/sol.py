class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = 10**6
        max_profit = 0

        for price in prices:
            if price < min_price_so_far:
                min_price_so_far = price

            profit = price - min_price_so_far

            if profit > max_profit:
                max_profit = profit
            
        return max_profit


        