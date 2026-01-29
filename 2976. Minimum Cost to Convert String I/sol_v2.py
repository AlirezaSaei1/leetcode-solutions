class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**18
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        # direct edges
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            if w < dist[u][v]:
                dist[u][v] = w

        # Floyd–Warshall
        for k in range(26):
            dk = dist[k]
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                ik = dist[i][k]
                di = dist[i]
                for j in range(26):
                    nd = ik + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        # sum costs
        total = 0
        for a, b in zip(source, target):
            if a == b:
                continue
            u = ord(a) - 97
            v = ord(b) - 97
            d = dist[u][v]
            if d >= INF:
                return -1
            total += d

        return total
