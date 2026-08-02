class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        
        def dp(L, R):
            if L > R:
                return 0
            if (L, R) in memo:
                return memo[(L, R)]
            
            take_left = piles[L] - dp(L + 1, R)
            take_right = piles[R] - dp(L, R - 1)
            
            memo[(L, R)] = max(take_left, take_right)
            return memo[(L, R)]
            
        return dp(0, len(piles) - 1) > 0