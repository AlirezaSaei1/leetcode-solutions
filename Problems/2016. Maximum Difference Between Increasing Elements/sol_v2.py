class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        ans = -1

        for x in nums[1:]:
            if x > min_so_far:
                ans = max(ans, x - min_so_far)
            else:
                min_so_far = x

        return ans