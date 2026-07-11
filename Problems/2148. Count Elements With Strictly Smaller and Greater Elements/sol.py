class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_val, max_val = float('inf'), float('-inf')
        min_count = max_count = 0
        
        for num in nums:
            if num < min_val:
                min_val = num
                min_count = 1
            elif num == min_val:
                min_count += 1
                
            if num > max_val:
                max_val = num
                max_count = 1
            elif num == max_val:
                max_count += 1
                
        if min_val == max_val:
            return 0
            
        return len(nums) - min_count - max_count