class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0
        ans = -10**18

        for i, x in enumerate(nums, 1):
            prefix += x
            r = i % k

            if min_prefix[r] != float('inf'):
                ans = max(ans, prefix - min_prefix[r])

            min_prefix[r] = min(min_prefix[r], prefix)

        return ans
