class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        unique_weights = set()
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            unique_weights.add(cost)
            
        q = [i for i in range(n) if in_degree[i] == 0]
        topo_order = []
        head = 0
        
        while head < len(q):
            u = q[head]
            head += 1
            topo_order.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        sorted_weights = sorted(list(unique_weights))
        
        if not sorted_weights:
            return -1
            
        def check(mid: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo_order:
                if dist[u] == float('inf'):
                    continue
                for v, cost in adj[u]:
                    if cost >= mid and online[v]:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            
            return dist[n-1] <= k

        if not check(0):
            return -1
            
        left, right = 0, len(sorted_weights) - 1
        ans = -1
        
        while left <= right:
            mid_idx = (left + right) // 2
            mid_val = sorted_weights[mid_idx]
            
            if check(mid_val):
                ans = mid_val
                left = mid_idx + 1
            else:
                right = mid_idx - 1
                
        return ans