class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp_prev_two = 0
        dp_prev_one = 0

        for i in range(2, n+1):
            cur = min(dp_prev_one + cost[i-1], dp_prev_two + cost[i-2])
            dp_prev_two, dp_prev_one = dp_prev_one, cur

        return dp_prev_one