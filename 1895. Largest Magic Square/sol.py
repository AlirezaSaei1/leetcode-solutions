class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Row and column prefix sums
        row_ps = [[0] * (n + 1) for _ in range(m)]
        col_ps = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j]
                col_ps[i + 1][j] = col_ps[i][j] + grid[i][j]

        # Diagonal prefix sums
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]  # top-left → bottom-right
        diag2 = [[0] * (n + 1) for _ in range(m + 1)]  # top-right → bottom-left

        for i in range(m):
            for j in range(n):
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        max_k = min(m, n)

        for k in range(max_k, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row_ps[i][j + k] - row_ps[i][j]

                    # Check rows
                    ok = True
                    for r in range(i, i + k):
                        if row_ps[r][j + k] - row_ps[r][j] != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    # Check columns
                    for c in range(j, j + k):
                        if col_ps[i + k][c] - col_ps[i][c] != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    # Check diagonals
                    if (
                        diag1[i + k][j + k] - diag1[i][j] != target or
                        diag2[i + k][j] - diag2[i][j + k] != target
                    ):
                        continue

                    return k

        return 1
