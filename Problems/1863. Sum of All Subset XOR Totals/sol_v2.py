class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        all_or = 0
        for x in nums:
            all_or |= x
        return all_or * (1 << (len(nums) - 1))