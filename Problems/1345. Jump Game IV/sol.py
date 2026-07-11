class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
            
        graph = {}
        for idx, val in enumerate(arr):
            if val not in graph:
                graph[val] = []
            graph[val].append(idx)
            
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            if idx == n - 1:
                return steps
                
            val = arr[idx]
            if val in graph:
                for next_idx in graph[val]:
                    if next_idx not in visited:
                        visited.add(next_idx)
                        queue.append((next_idx, steps + 1))
                del graph[val]
                
            if idx + 1 < n and (idx + 1) not in visited:
                visited.add(idx + 1)
                queue.append((idx + 1, steps + 1))
                
            if idx - 1 >= 0 and (idx - 1) not in visited:
                visited.add(idx - 1)
                queue.append((idx - 1, steps + 1))
                
        return -1