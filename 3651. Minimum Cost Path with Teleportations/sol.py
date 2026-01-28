class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**30
        VMAX = 10000

        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0

        for t in range(k + 1):
            # 1) Relax normal moves (right/down) in DAG order
            for i in range(m):
                for j in range(n):
                    d = dist[i][j]
                    if d >= INF:
                        continue
                    if i + 1 < m:
                        nd = d + grid[i + 1][j]
                        if nd < dist[i + 1][j]:
                            dist[i + 1][j] = nd
                    if j + 1 < n:
                        nd = d + grid[i][j + 1]
                        if nd < dist[i][j + 1]:
                            dist[i][j + 1] = nd

            if t == k:
                return dist[m - 1][n - 1]

            # 2) Prepare next layer (at most t+1 teleports): start with "don't teleport"
            nxt = [row[:] for row in dist]

            # 3) Bulk-apply teleport transitions:
            #    From any cell with value >= w, we can teleport to any cell with value w at cost 0.
            best_at = [INF] * (VMAX + 1)
            for i in range(m):
                for j in range(n):
                    v = grid[i][j]
                    d = dist[i][j]
                    if d < best_at[v]:
                        best_at[v] = d

            for v in range(VMAX - 1, -1, -1):
                if best_at[v + 1] < best_at[v]:
                    best_at[v] = best_at[v + 1]

            for i in range(m):
                for j in range(n):
                    w = grid[i][j]
                    bd = best_at[w]
                    if bd < nxt[i][j]:
                        nxt[i][j] = bd

            dist = nxt

        return dist[m - 1][n - 1]
