class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthiest = 0
        for customer in accounts:
            wealthiest = max(sum(customer), wealthiest)
        
        return wealthiest