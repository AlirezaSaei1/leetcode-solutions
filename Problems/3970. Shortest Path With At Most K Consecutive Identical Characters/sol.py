class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0
            
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        K_PLUS_1 = k + 1
        dist = [float('inf')] * (n * K_PLUS_1)
        dist[1] = 0 
        
        pq = [(0, 0, 1)] 
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if d > dist[u * K_PLUS_1 + count]:
                continue
                
            if u == n - 1:
                return d
                
            label_u = labels[u]
            for v, w in adj[u]:
                next_count = count + 1 if label_u == labels[v] else 1
                
                if next_count <= k:
                    next_d = d + w
                    idx = v * K_PLUS_1 + next_count
                    if next_d < dist[idx]:
                        dist[idx] = next_d
                        heapq.heappush(pq, (next_d, v, next_count))
                        
        return -1