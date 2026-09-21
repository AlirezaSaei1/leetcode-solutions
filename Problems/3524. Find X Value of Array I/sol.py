class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        dp = [0] * k

        for x in nums:
            v = x % k
            next_dp = [0] * k
            next_dp[v] += 1

            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * v) % k] += dp[r]

            dp = next_dp

            for r in range(k):
                result[r] += dp[r]

        return result