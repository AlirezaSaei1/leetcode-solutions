class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def flood(r: int, c: int):
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                curr_r, curr_c = stack.pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr, nc))
                        
        for r in range(rows):
            for c in (0, cols - 1):
                if grid[r][c] == 0:
                    flood(r, c)
                    
        for c in range(cols):
            for r in (0, rows - 1):
                if grid[r][c] == 0:
                    flood(r, c)
                    
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    flood(r, c)
                    
        return closed_islands