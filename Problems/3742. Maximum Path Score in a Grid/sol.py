class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                cell_cost = 0 if val == 0 else 1
                cell_score = val
                
                for c in range(k + 1):
                    if dp[i][j][c] == -1:
                        continue
                    
                    current_score = dp[i][j][c]
                    
                    # Try moving Right
                    if j + 1 < n:
                        next_val = grid[i][j+1]
                        next_cost = c + (0 if next_val == 0 else 1)
                        if next_cost <= k:
                            dp[i][j+1][next_cost] = max(dp[i][j+1][next_cost], current_score + next_val)
                            
                    # Try moving Down
                    if i + 1 < m:
                        next_val = grid[i+1][j]
                        next_cost = c + (0 if next_val == 0 else 1)
                        if next_cost <= k:
                            dp[i+1][j][next_cost] = max(dp[i+1][j][next_cost], current_score + next_val)

        ans = max(dp[m-1][n-1])
        return ans if ans != -1 else -1