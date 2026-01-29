class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[] for _ in range(26)]
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            graph[u].append((v, w))

        INF = 10**18
        memo = {}

        def min_cost(a: str, b: str) -> int:
            if a == b:
                return 0
            key = (a, b)
            if key in memo:
                return memo[key]

            src = ord(a) - 97
            dst = ord(b) - 97

            dist = [INF] * 26
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                d, u = heapq.heappop(pq)
                if u == dst:
                    memo[key] = d
                    return d
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))

            memo[key] = -1
            return -1
        
        total_cost = 0
        n = len(source)
        for i in range(n):
            cost = min_cost(source[i], target[i])
            if cost == -1:
                return -1
            else:
                total_cost += cost
        
        return total_cost