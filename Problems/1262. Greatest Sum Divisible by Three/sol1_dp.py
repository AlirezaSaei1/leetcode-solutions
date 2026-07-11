class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        NEG_INF = float('-inf')
        dp = [0, NEG_INF, NEG_INF]

        for x in nums:
            new_dp = dp[:]

            for r in range(3):
                if new_dp[r] == NEG_INF:
                    continue
                
                new_r = (r + x % 3) % 3

                new_dp[new_r] = max(new_dp[new_r], dp[r] + x)

            dp = new_dp

        return dp[0]