class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # 1. Build the adjacency list for the tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Use BFS to find the maximum depth from root node 1
        queue = deque([(1, 0)])
        visited = {1}
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
                
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
        # 3. Calculate 2^(max_depth - 1) % MOD using fast modular exponentiation
        return pow(2, max_depth - 1, MOD)