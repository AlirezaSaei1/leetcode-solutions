class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        suffix_min = [0] * n

        for i in range(n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        minn = float('inf')
        for i in range(n-1, -1, -1):
            if minn > nums[i]:
                minn = nums[i]
            suffix_min[i] = minn

        score = []
        for i in range(n-1):
            score.append(prefix_sum[i] - suffix_min[i+1])
        return max(score)