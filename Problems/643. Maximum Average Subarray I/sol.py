class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        cur_sum = 0

        for i in range(0, len(nums)):
            if i < k:
                cur_sum += nums[i]
            else:
                cur_sum += nums[i]
                cur_sum -= nums[i-k]

            if i >= k - 1:
                max_sum = max(max_sum, cur_sum)
            
        return max_sum / k