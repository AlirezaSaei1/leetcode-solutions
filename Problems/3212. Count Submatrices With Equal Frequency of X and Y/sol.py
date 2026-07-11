class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        prefX = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefY = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                is_x = 1 if grid[r][c] == 'X' else 0
                is_y = 1 if grid[r][c] == 'Y' else 0
                
                prefX[r+1][c+1] = is_x + prefX[r][c+1] + prefX[r+1][c] - prefX[r][c]
                prefY[r+1][c+1] = is_y + prefY[r][c+1] + prefY[r+1][c] - prefY[r][c]
                
                if prefX[r+1][c+1] == prefY[r+1][c+1] and prefX[r+1][c+1] > 0:
                    count += 1
                    
        return count