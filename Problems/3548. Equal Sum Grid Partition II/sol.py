class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        
        row_sums = [sum(row) for row in grid]
        col_sums = [0] * n
        for r in range(m):
            for c in range(n):
                col_sums[c] += grid[r][c]

        def get_row_counts(r_idx):
            return Counter(grid[r_idx])

        def get_col_counts(c_idx):
            counts = Counter()
            for r in range(m):
                counts[grid[r][c_idx]] += 1
            return counts

        # Horizontal Cuts
        full_grid_counts = Counter()
        for r in range(m):
            for c in range(n):
                full_grid_counts[grid[r][c]] += 1
        
        top_counts = Counter()
        top_sum = 0
        for i in range(m - 1):
            top_sum += row_sums[i]
            for val in grid[i]:
                top_counts[val] += 1
            
            bottom_sum = total_sum - top_sum
            diff = abs(top_sum - bottom_sum)
            
            if diff == 0: return True
            
            if top_sum > bottom_sum:
                if i == 0: # Single row: only ends
                    if grid[0][0] == diff or grid[0][n-1] == diff: return True
                elif n == 1: # Single column: only ends
                    if grid[0][0] == diff or grid[i][0] == diff: return True
                elif top_counts[diff] > 0: return True
            else:
                if i == m - 2: # Single row: only ends
                    if grid[m-1][0] == diff or grid[m-1][n-1] == diff: return True
                elif n == 1: # Single column: only ends
                    if grid[i+1][0] == diff or grid[m-1][0] == diff: return True
                elif (full_grid_counts[diff] - top_counts[diff]) > 0: return True

        # Vertical Cuts
        left_counts = Counter()
        left_sum = 0
        for j in range(n - 1):
            left_sum += col_sums[j]
            for r in range(m):
                left_counts[grid[r][j]] += 1
                
            right_sum = total_sum - left_sum
            diff = abs(left_sum - right_sum)
            
            if diff == 0: return True
            
            if left_sum > right_sum:
                if j == 0: # Single col
                    if grid[0][0] == diff or grid[m-1][0] == diff: return True
                elif m == 1: # Single row
                    if grid[0][0] == diff or grid[0][j] == diff: return True
                elif left_counts[diff] > 0: return True
            else:
                if j == n - 2: # Single col
                    if grid[0][n-1] == diff or grid[m-1][n-1] == diff: return True
                elif m == 1: # Single row
                    if grid[0][j+1] == diff or grid[0][n-1] == diff: return True
                elif (full_grid_counts[diff] - left_counts[diff]) > 0: return True

        return False