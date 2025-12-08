class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)

        flat = [num for row in grid for num in row]
        flat = flat[-k:] + flat[:-k]
        new_grid = []
        for i in range(m):
            new_grid.append(flat[i*n : (i+1)*n])

        return new_grid