class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = coins[0][0]

        if coins[0][0] < 0:
            dp[0][0][1] = 0
            
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                for k in range(3):
                    prev_max = -float('inf')
                    if i > 0: prev_max = max(prev_max, dp[i-1][j][k])
                    if j > 0: prev_max = max(prev_max, dp[i][j-1][k])
                    
                    if prev_max != -float('inf'):
                        dp[i][j][k] = max(dp[i][j][k], prev_max + coins[i][j])
                    
                    if coins[i][j] < 0 and k > 0:
                        prev_k_max = -float('inf')
                        if i > 0: prev_k_max = max(prev_k_max, dp[i-1][j][k-1])
                        if j > 0: prev_k_max = max(prev_k_max, dp[i][j-1][k-1])
                        
                        if prev_k_max != -float('inf'):
                            dp[i][j][k] = max(dp[i][j][k], prev_k_max)

        return max(dp[m-1][n-1])