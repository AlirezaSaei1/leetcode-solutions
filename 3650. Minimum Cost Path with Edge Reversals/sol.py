class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        out = [[] for _ in range(n)]
        inc = [[] for _ in range(n)]

        for u, v, w in edges:
            out[u].append((v, w))
            inc[v].append((u, w))

        INF = 10**30
        dist0 = [INF] * n
        dist1 = [INF] * n
        dist0[0] = 0

        pq = [(0, 0, 0)]

        while pq:
            d, u, used = heapq.heappop(pq)
            if used == 0:
                if d != dist0[u]:
                    continue
            else:
                if d != dist1[u]:
                    continue

            for v, w in out[u]:
                nd = d + w
                if nd < dist0[v]:
                    dist0[v] = nd
                    heapq.heappush(pq, (nd, v, 0))

            if used == 0:
                if d < dist1[u]:
                    dist1[u] = d
                    heapq.heappush(pq, (d, u, 1))

                for v, w in inc[u]:
                    nd = d + 2 * w
                    if nd < dist0[v]:
                        dist0[v] = nd
                        heapq.heappush(pq, (nd, v, 0))

        ans = min(dist0[n - 1], dist1[n - 1])
        return -1 if ans >= INF else ans
