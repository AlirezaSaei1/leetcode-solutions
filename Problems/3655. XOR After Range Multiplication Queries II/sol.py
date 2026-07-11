class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        bravexuneth = queries
        T = int(n**0.5)
        
        small_k_groups = [[] for _ in range(T)]
        
        for l, r, k, v in bravexuneth:
            if v == 1: 
                continue
            if k >= T:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                small_k_groups[k].append((l, r, v))
        
        diff = [1] * (n + T)
        
        for k in range(1, T):
            if not small_k_groups[k]:
                continue
            
            for i in range(n + k):
                diff[i] = 1
                
            for l, r, v in small_k_groups[k]:
                diff[l] = (diff[l] * v) % MOD
                steps = (r - l) // k + 1
                R = l + steps * k
                diff[R] = (diff[R] * pow(v, MOD - 2, MOD)) % MOD
            
            for i in range(k, n):
                diff[i] = (diff[i] * diff[i - k]) % MOD
            
            for i in range(n):
                if diff[i] != 1:
                    nums[i] = (nums[i] * diff[i]) % MOD
        
        ans = 0
        for x in nums:
            ans ^= x
            
        return ans