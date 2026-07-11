class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        factory_slots = []
        for pos, limit in factory:
            factory_slots.extend([pos] * limit)
        
        n, m = len(robot), len(factory_slots)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        for j in range(m + 1):
            dp[0][j] = 0
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                res = dp[i][j-1]
                take = dp[i-1][j-1] + abs(robot[i-1] - factory_slots[j-1])
                dp[i][j] = min(res, take)
                
        return dp[n][m]