class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        INF = 10**18

        # 1) Group rules by length
        rules_by_len = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            L = len(o)
            rules_by_len[L].append((o, c, w))

        # 2) For each length L, build Floyd–Warshall dist over strings
        dist_by_len: Dict[int, List[List[int]]] = {}
        idx_by_len: Dict[int, Dict[str, int]] = {}

        for L, rules in rules_by_len.items():
            nodes = set()
            for o, c, _ in rules:
                nodes.add(o)
                nodes.add(c)
            nodes = list(nodes)

            idx = {s: i for i, s in enumerate(nodes)}
            m = len(nodes)

            dist = [[INF] * m for _ in range(m)]
            for i in range(m):
                dist[i][i] = 0

            for o, c, w in rules:
                u, v = idx[o], idx[c]
                if w < dist[u][v]:
                    dist[u][v] = w

            # Floyd–Warshall
            for k in range(m):
                dk = dist[k]
                for i in range(m):
                    if dist[i][k] >= INF:
                        continue
                    ik = dist[i][k]
                    di = dist[i]
                    for j in range(m):
                        nd = ik + dk[j]
                        if nd < di[j]:
                            di[j] = nd

            dist_by_len[L] = dist
            idx_by_len[L] = idx

        # 3) DP over positions
        dp = [INF] * (n + 1)
        dp[0] = 0

        lengths = list(dist_by_len.keys())

        for i in range(n):
            if dp[i] >= INF:
                continue

            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for L in lengths:
                if i + L > n:
                    continue
                a = source[i:i + L]
                b = target[i:i + L]
                if a == b:
                    dp[i + L] = min(dp[i + L], dp[i])
                    continue

                idx = idx_by_len[L]
                if a not in idx or b not in idx:
                    continue

                d = dist_by_len[L][idx[a]][idx[b]]
                if d < INF:
                    dp[i + L] = min(dp[i + L], dp[i] + d)

        return -1 if dp[n] >= INF else dp[n]
