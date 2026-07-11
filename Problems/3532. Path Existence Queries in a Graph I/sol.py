class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        if n == 0:
            return [False] * len(queries)
        
        component_id = [0] * n
        current_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                current_id += 1
            component_id[i] = current_id
            
        results = []
        for u, v in queries:
            results.append(component_id[u] == component_id[v])
            
        return results