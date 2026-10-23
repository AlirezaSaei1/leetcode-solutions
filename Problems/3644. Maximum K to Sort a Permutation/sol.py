class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        k = -1
        
        for i, val in enumerate(nums):
            if i != val:
                k &= val
                
        return 0 if k == -1 else k