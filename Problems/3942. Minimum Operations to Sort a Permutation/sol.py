class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0

        idx = 0
        for i in range(n):
            if nums[i] == 0:
                idx = i
                break

        is_inc = True
        for k in range(n):
            if nums[(idx + k) % n] != k:
                is_inc = False
                break
                
        is_dec = True
        for k in range(n):
            if nums[(idx - k) % n] != k:
                is_dec = False
                break
                
        if not is_inc and not is_dec:
            return -1
            
        min_ops = float('inf')
        
        if is_inc:
            i = idx
            min_ops = min(min_ops, i, n - i + 2)
            
        if is_dec:
            i = (n - 1 - idx) % n
            min_ops = min(min_ops, i + 1, n - i + 1)
            
        return min_ops