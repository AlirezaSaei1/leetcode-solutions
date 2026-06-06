class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        cur_sum = 0
        for i in range(n):
            left_sum[i] = cur_sum
            cur_sum += nums[i]
            right_sum[i] = total_sum - cur_sum
        
        return [abs(left - right) for left, right in zip(left_sum, right_sum)]