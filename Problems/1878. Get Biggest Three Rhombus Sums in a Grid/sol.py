class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        unique_sums = set()

        for r in range(rows):
            for c in range(cols):
                unique_sums.add(grid[r][c])
                
                for s in range(1, 50):
                    # Define the 4 corners
                    top = (r, c)
                    right = (r + s, c + s)
                    bottom = (r + 2 * s, c)
                    left = (r + s, c - s)
                    
                    if not (bottom[0] < rows and left[1] >= 0 and right[1] < cols):
                        break
                    
                    current_sum = 0
                    
                    # 1. Top to Right
                    for i in range(s):
                        current_sum += grid[top[0] + i][top[1] + i]
                    # 2. Right to Bottom
                    for i in range(s):
                        current_sum += grid[right[0] + i][right[1] - i]
                    # 3. Bottom to Left
                    for i in range(s):
                        current_sum += grid[bottom[0] - i][bottom[1] - i]
                    # 4. Left to Top
                    for i in range(s):
                        current_sum += grid[left[0] - i][left[1] + i]
                        
                    unique_sums.add(current_sum)
        
        return sorted(list(unique_sums), reverse=True)[:3]