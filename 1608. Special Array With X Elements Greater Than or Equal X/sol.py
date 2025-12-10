class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            x = n - i
            if nums[i] >= x and (i == 0 or nums[i-1] < x):
                return x
        
        return -1