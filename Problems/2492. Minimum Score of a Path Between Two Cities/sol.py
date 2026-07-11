class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, distance in roads:
            adj[u].append((v, distance))
            adj[v].append((u, distance))
            
        global_min = float('inf')
        visited = set()

        def dfs(node):
            nonlocal global_min
            visited.add(node)

            for neighbor, distance in adj[node]:
                global_min = min(global_min, distance)
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(1)
        return global_min
        
