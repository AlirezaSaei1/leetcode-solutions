class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row_servers = [0] * m
        col_servers = [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_servers[i] += 1
                    col_servers[j] += 1
                    
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_servers[i] > 1 or col_servers[j] > 1:
                        ans += 1
                        
        return ans