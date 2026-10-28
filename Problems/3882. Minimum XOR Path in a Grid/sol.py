class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [set() for _ in range(n)]
        
        dp[0].add(grid[0][0])
        
        for j in range(1, n):
            val = grid[0][j]
            dp[j] = {x ^ val for x in dp[j-1]}
            
        for i in range(1, m):
            val = grid[i][0]
            dp[0] = {x ^ val for x in dp[0]}
            
            for j in range(1, n):
                val = grid[i][j]
                dp[j] = {x ^ val for x in (dp[j] | dp[j-1])}
                
        return min(dp[-1])