class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        max_sum = float('-inf')

        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[~i])
        
        return max_sum