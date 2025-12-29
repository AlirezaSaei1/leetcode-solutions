class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        
        total = 7 * weeks * (weeks + 1) // 2 + 21 * weeks
        total += days * (2 * (weeks + 1) + (days - 1)) // 2
        
        return total
