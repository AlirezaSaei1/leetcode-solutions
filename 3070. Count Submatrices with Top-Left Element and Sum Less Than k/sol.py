class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        prefix_sum = [[0] * cols for _ in range(rows)]
        count = 0

        for r in range(rows):
            for c in range(cols):
                current_val = grid[r][c]
                top = prefix_sum[r-1][c] if r > 0 else 0
                left = prefix_sum[r][c-1] if c > 0 else 0
                overlap = prefix_sum[r-1][c-1] if (r > 0 and c > 0) else 0
                
                prefix_sum[r][c] = current_val + top + left - overlap
                
                if prefix_sum[r][c] <= k:
                    count += 1
                else:
                    pass
                    
        return count