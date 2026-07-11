class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface = 0
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h > 0:
                    surface += h * 6
                    surface -= (h - 1) * 2
                
                if j + 1 < n:
                    surface -= 2 * min(h, grid[i][j + 1])
                    
                if i + 1 < n:
                    surface -= 2 * min(h, grid[i + 1][j])
        
        return surface
