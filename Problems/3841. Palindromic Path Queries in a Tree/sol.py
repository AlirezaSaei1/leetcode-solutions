class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 16
        tin = [0] * n
        depth = [0] * n
        up = [[0] * LOG for _ in range(n)]
        initial_X = [0] * n
        current_chars = [1 << (ord(c) - 97) for c in s]
        
        initial_X[0] = current_chars[0]
        
        parent = [-1] * n
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True
        
        timer = 1
        while stack:
            u = stack.pop()
            order.append(u)
            tin[u] = timer
            timer += 1
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    for i in range(1, LOG):
                        up[v][i] = up[up[v][i-1]][i-1]
                    initial_X[v] = initial_X[u] ^ current_chars[v]
                    stack.append(v)
                    
        tout = list(tin)
        for u in reversed(order):
            if parent[u] != -1:
                if tout[u] > tout[parent[u]]:
                    tout[parent[u]] = tout[u]
                    
        bit = [0] * (n + 2)
        
        def add(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query_bit(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                diff = current_chars[u] ^ new_mask
                if diff != 0:
                    add(tin[u], diff)
                    add(tout[u] + 1, diff)
                    current_chars[u] = new_mask
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                Xu = initial_X[u] ^ query_bit(tin[u])
                Xv = initial_X[v] ^ query_bit(tin[v])
                lca_char = current_chars[lca]
                
                path_mask = Xu ^ Xv ^ lca_char
                
                is_palin = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palin)
                
        return ans