class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        for a, b in allowedSwaps:
            union(a, b)
            
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
            
        total_matches = 0
        for indices in components.values():
            s_counts = Counter(source[i] for i in indices)
            t_counts = Counter(target[i] for i in indices)
            
            for val in s_counts:
                if val in t_counts:
                    total_matches += min(s_counts[val], t_counts[val])
        
        return n - total_matches