class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        
        base = sum(s * p for s, p in zip(strategy, prices))
        
        pref_price = [0] * (n + 1)
        pref_profit = [0] * (n + 1)
        
        for i in range(n):
            pref_price[i + 1] = pref_price[i] + prices[i]
            pref_profit[i + 1] = pref_profit[i] + strategy[i] * prices[i]
        
        best = base
        half = k // 2
        
        for l in range(0, n - k + 1):
            mid = l + half
            r = l + k
            
            old_profit = pref_profit[r] - pref_profit[l]
            
            new_profit = pref_price[r] - pref_price[mid]
            
            delta = new_profit - old_profit
            best = max(best, base + delta)
        
        return best
