class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        prev = [[0] * k for _ in range(n)]
        
        for i in range(m):
            cur = [[0] * k for _ in range(n)]
            for j in range(n):
                v_mod = grid[i][j] % k
                
                if i == 0 and j == 0:
                    cur[0][v_mod] = 1
                    continue
                
                for r in range(k):
                    if i > 0:
                        cnt_top = prev[j][r]
                        if cnt_top:
                            new_r = (r + v_mod) % k
                            cur[j][new_r] = (cur[j][new_r] + cnt_top) % MOD
                    
                    if j > 0:
                        cnt_left = cur[j - 1][r]
                        if cnt_left:
                            new_r = (r + v_mod) % k
                            cur[j][new_r] = (cur[j][new_r] + cnt_left) % MOD
            
            prev = cur
        
        return prev[n - 1][0]
