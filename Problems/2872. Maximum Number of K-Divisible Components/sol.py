class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        self.components = 0

        def dfs(u, parent):
            subtotal = values[u]

            for v in adj[u]:
                if v == parent:
                    continue
                subtotal += dfs(v, u)

            if subtotal % k == 0:
                self.components += 1
                return 0

            return subtotal % k

        dfs(0, -1)
        return self.components