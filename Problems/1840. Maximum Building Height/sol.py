class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        m = len(restrictions)
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + (restrictions[i][0] - restrictions[i-1][0]))

        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0]))
        
        max_h = 0
        for i in range(m - 1):
            idx1, h1 = restrictions[i]
            idx2, h2 = restrictions[i+1]
            
            dist = idx2 - idx1
            peak = (h1 + h2 + dist) // 2
            max_h = max(max_h, peak)
            
        max_h = max(max_h, restrictions[-1][1] + (n - restrictions[-1][0]))
        return max_h
