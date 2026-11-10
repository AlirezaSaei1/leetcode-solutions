class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp_3, dp_2, dp_1 = float('inf'), float('inf'), 0
        
        for i in range(1, n + 1):
            cost_here = costs[i - 1]
            
            current_dp = min(
                dp_1 + cost_here + 1,
                dp_2 + cost_here + 4,
                dp_3 + cost_here + 9
            )

            dp_3, dp_2, dp_1 = dp_2, dp_1, current_dp
            
        return dp_1