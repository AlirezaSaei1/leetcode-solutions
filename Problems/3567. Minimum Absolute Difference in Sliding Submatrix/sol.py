class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = m - k + 1, n - k + 1
        ans = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                elements = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        elements.append(grid[r][c])
                
                elements.sort()
                
                min_diff = float('inf')
                found_distinct_diff = False
                
                for idx in range(len(elements) - 1):
                    diff = elements[idx+1] - elements[idx]
                    if diff > 0:
                        if diff < min_diff:
                            min_diff = diff
                        found_distinct_diff = True
                
                ans[i][j] = min_diff if found_distinct_diff else 0
                    
        return ans