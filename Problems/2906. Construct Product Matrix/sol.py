class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]
        MOD = 12345
        
        # Forward Pass: Calculate Prefix Products
        running_prod = 1
        for r in range(n):
            for c in range(m):
                p[r][c] = running_prod
                running_prod = (running_prod * grid[r][c]) % MOD
                
        # Backward Pass: Multiply by Suffix Products
        running_prod = 1
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                p[r][c] = (p[r][c] * running_prod) % MOD
                running_prod = (running_prod * grid[r][c]) % MOD
                
        return p