class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        prev = nums[0]
        for x in nums[1:]:
            if x <= prev:
                ops += prev + 1 - x
                prev = prev + 1
            else:
                prev = x
        return ops
