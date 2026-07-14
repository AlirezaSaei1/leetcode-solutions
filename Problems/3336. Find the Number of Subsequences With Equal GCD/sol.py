class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        dp = defaultdict(int)
        dp[(0, 0)] = 1
        
        for x in nums:
            new_dp = dp.copy()
            for (g1, g2), count in dp.items():
                # Add to seq1
                new_g1 = x if g1 == 0 else gcd(g1, x)
                new_dp[(new_g1, g2)] = (new_dp[(new_g1, g2)] + count) % MOD
                
                # Add to seq2
                new_g2 = x if g2 == 0 else gcd(g2, x)
                new_dp[(g1, new_g2)] = (new_dp[(g1, new_g2)] + count) % MOD
            dp = new_dp
            
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 > 0 and g1 == g2:
                ans = (ans + count) % MOD
                
        return ans