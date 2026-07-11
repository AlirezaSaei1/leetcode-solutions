class Solution:
    def arrangeCoins(self, n: int) -> int:
        delta = 1 + 8 * n
        return floor((-1 + sqrt(delta)) / 2)
        
