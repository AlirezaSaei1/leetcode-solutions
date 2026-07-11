class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            nums.extend(row)
        
        nums.sort()
        n = len(nums)
        
        rem = nums[0] % x
        for num in nums:
            if num % x != rem:
                return -1
        
        median = nums[n // 2]
        
        ops = 0
        for num in nums:
            ops += abs(num - median) // x
            
        return ops