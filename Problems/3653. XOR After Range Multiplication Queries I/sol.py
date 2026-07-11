class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        for li, ri, ki, vi in queries:
            for idx in range(li, ri + 1, ki):
                nums[idx] = (nums[idx] * vi) % MOD
        
        res = 0
        for num in nums:
            res ^= num
            
        return res