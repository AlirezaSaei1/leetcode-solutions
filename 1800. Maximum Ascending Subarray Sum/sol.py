class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum, max_sum = nums[0], 0
        n = len(nums)

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                cur_sum += nums[i]
            else:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[i]
        
        return max(max_sum, cur_sum)