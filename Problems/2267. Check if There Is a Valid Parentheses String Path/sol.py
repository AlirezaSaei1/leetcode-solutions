class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_len = m + n - 1

        if total_len % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        max_bal = total_len // 2

        @lru_cache(None)
        def dfs(r: int, c: int, bal: int) -> bool:
            bal += 1 if grid[r][c] == '(' else -1

            if bal < 0 or bal > max_bal:
                return False

            # Base Case: Reached bottom-right cell
            if r == m - 1 and c == n - 1:
                return bal == 0

            # Move Down
            if r + 1 < m and dfs(r + 1, c, bal):
                return True
            # Move Right
            if c + 1 < n and dfs(r, c + 1, bal):
                return True

            return False

        return dfs(0, 0, 0)