class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                component = []
                queue = deque([i])
                visited[i] = True

                while queue:
                    u = queue.popleft()
                    component.append(u)

                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)
                    
                v_count = len(component)
                is_complete = True
                for node in component:
                    if len(adj[node]) != v_count - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    count += 1
                    
        return count


