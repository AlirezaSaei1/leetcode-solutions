class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = 0

        def magic(r, c):
            if grid[r + 1][c + 1] != 5:
                return False

            seen = set()
            for i in range(3):
                for j in range(3):
                    v = grid[r+i][c+j]
                    if v < 1 or v > 9 or v in seen:
                        return False
                    seen.add(v)
            
            s = 15
            return (
                grid[r][c] + grid[r][c+1] + grid[r][c+2] == s and
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == s and
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == s and
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == s and
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == s and
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == s and
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == s and
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == s
            )

        for i in range(n - 2):
            for j in range(m - 2):
                if magic(i, j):
                    answer += 1
        return answer