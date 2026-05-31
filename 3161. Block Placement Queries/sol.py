class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * size
        self.size = size

    def update(self, i, val):
        while i < self.size:
            if val > self.tree[i]:
                self.tree[i] = val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            if self.tree[i] > res:
                res = self.tree[i]
            i -= i & -i
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = min(50000, len(queries) * 3)
        limit = max_x + 1
        
        obstacles = [0, limit]
        type1_set = set()
        
        for q in queries:
            if q[0] == 1:
                type1_set.add(q[1])
                obstacles.append(q[1])
                
        obstacles.sort()
        
        ft = FenwickTree(limit + 2)
        
        for i in range(1, len(obstacles)):
            ft.update(obstacles[i], obstacles[i] - obstacles[i - 1])
            
        ans = []
        
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                
                low, high = 0, len(obstacles) - 1
                idx = 0
                while low <= high:
                    mid = (low + high) // 2
                    if obstacles[mid] >= x:
                        idx = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                        
                prev_val = obstacles[idx - 1]
                next_val = obstacles[idx + 1]
                
                obstacles.pop(idx)
                ft.update(next_val, next_val - prev_val)
            else:
                x, sz = q[1], q[2]
                
                low, high = 0, len(obstacles) - 1
                idx = len(obstacles)
                while low <= high:
                    mid = (low + high) // 2
                    if obstacles[mid] >= x:
                        idx = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                        
                prev_val = obstacles[idx - 1]
                
                max_gap = ft.query(prev_val)
                if x - prev_val > max_gap:
                    max_gap = x - prev_val
                    
                ans.append(max_gap >= sz)
                
        return ans[::-1]
