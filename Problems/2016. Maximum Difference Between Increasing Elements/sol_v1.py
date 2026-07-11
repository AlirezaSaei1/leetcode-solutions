class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -1
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n):
                diff = nums[j] - nums[i]
                if diff > 0:
                    answer = max(answer, diff)

        return answer  