class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def path_exists(node):
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbor in graph_map[node]:
                if neighbor not in visited:
                    if path_exists(neighbor):
                        return True
            
            return False

        graph_map = defaultdict(list)
        for u, v in edges:
            graph_map[u].append(v)
            graph_map[v].append(u)
        
        visited = set()
        
        return path_exists(source)