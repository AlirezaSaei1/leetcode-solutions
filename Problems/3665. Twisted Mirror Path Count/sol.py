class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        tgt_r = [[[-1, -1] for _ in range(n)] for _ in range(m)]
        tgt_c = [[[-1, -1] for _ in range(n)] for _ in range(m)]
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    tgt_r[r][c][0] = r
                    tgt_c[r][c][0] = c
                    tgt_r[r][c][1] = r
                    tgt_c[r][c][1] = c
                else:
                    if r + 1 < m:
                        tgt_r[r][c][0] = tgt_r[r + 1][c][1]
                        tgt_c[r][c][0] = tgt_c[r + 1][c][1]
                        
                    if c + 1 < n:
                        tgt_r[r][c][1] = tgt_r[r][c + 1][0]
                        tgt_c[r][c][1] = tgt_c[r][c + 1][0]
                        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if not dp[r][c] or grid[r][c] == 1:
                    continue
                    
                ways = dp[r][c]
                
                if c + 1 < n:
                    tr = tgt_r[r][c + 1][0]
                    tc = tgt_c[r][c + 1][0]
                    if tr != -1:
                        dp[tr][tc] = (dp[tr][tc] + ways) % MOD
                        
                if r + 1 < m:
                    tr = tgt_r[r + 1][c][1]
                    tc = tgt_c[r + 1][c][1]
                    if tr != -1:
                        dp[tr][tc] = (dp[tr][tc] + ways) % MOD
                        
        return dp[m - 1][n - 1] # BOOOOOO