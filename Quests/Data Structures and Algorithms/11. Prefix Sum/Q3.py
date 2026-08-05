class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        suffix_even = sum(nums[0::2])
        suffix_odd = sum(nums[1::2])
        
        prefix_even = 0
        prefix_odd = 0
        fair_count = 0
        
        for i, num in enumerate(nums):
            if i % 2 == 0:
                suffix_even -= num
            else:
                suffix_odd -= num
                
            if prefix_even + suffix_odd == prefix_odd + suffix_even:
                fair_count += 1
                
            if i % 2 == 0:
                prefix_even += num
            else:
                prefix_odd += num
                
        return fair_count