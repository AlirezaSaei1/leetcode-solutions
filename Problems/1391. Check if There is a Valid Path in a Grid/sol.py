class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        directions = {
            1: [(0, -1), (0, 1)],  # Left, Right
            2: [(-1, 0), (1, 0)],  # Up, Down
            3: [(0, -1), (1, 0)],  # Left, Down
            4: [(0, 1), (1, 0)],   # Right, Down
            5: [(0, -1), (-1, 0)], # Left, Up
            6: [(0, 1), (-1, 0)]   # Right, Up
        }

        stack = [(0, 0)]
        visited = {(0, 0)}
        
        while stack:
            x, y = stack.pop()
            if x == m - 1 and y == n - 1:
                return True
            
            st_type = grid[x][y]
            for dx, dy in directions[st_type]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    neighbor_st = grid[nx][ny]
                    if (-dx, -dy) in directions[neighbor_st]:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        
        return False