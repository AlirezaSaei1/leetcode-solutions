class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx, max_idx = 0, 0
        min_val, max_val = float('inf'), float('-inf')

        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i

            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i

        left_idx = min(min_idx, max_idx)
        right_idx = max(min_idx, max_idx)

        option1 = right_idx + 1
        option2 = n - left_idx
        option3 = (left_idx + 1) + (n - right_idx)

        return min(option1, option2, option3)