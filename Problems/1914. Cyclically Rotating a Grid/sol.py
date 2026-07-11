class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            r_min, r_max = layer, m - 1 - layer
            c_min, c_max = layer, n - 1 - layer
            
            h = r_max - r_min + 1
            w = c_max - c_min + 1
            total_elements = 2 * (h + w) - 4
            
            shift = k % total_elements
            if shift == 0:
                continue
                
            layer_vals = []
            for col in range(c_min, c_max + 1):
                layer_vals.append(grid[r_min][col])
            for row in range(r_min + 1, r_max + 1):
                layer_vals.append(grid[row][c_max])
            for col in range(c_max - 1, c_min - 1, -1):
                layer_vals.append(grid[r_max][col])
            for row in range(r_max - 1, r_min, -1):
                layer_vals.append(grid[row][c_min])
                
            idx = shift
            for col in range(c_min, c_max + 1):
                grid[r_min][col] = layer_vals[idx]
                idx = (idx + 1) % total_elements
            for row in range(r_min + 1, r_max + 1):
                grid[row][c_max] = layer_vals[idx]
                idx = (idx + 1) % total_elements
            for col in range(c_max - 1, c_min - 1, -1):
                grid[r_max][col] = layer_vals[idx]
                idx = (idx + 1) % total_elements
            for row in range(r_max - 1, r_min, -1):
                grid[row][c_min] = layer_vals[idx]
                idx = (idx + 1) % total_elements
                
        return grid