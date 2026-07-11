class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        nz_indices = [i for i, char in enumerate(s) if char != '0']
        nz_vals = [int(s[i]) for i in nz_indices]
        num_nz = len(nz_vals)
        
        if num_nz == 0:
            return [0] * len(queries)

        pref_sum = [0] + list(accumulate(nz_vals))
        
        pref_cat = [0] * (num_nz + 1)
        pow10 = [1] * (num_nz + 1)
        for i in range(num_nz):
            pref_cat[i+1] = (pref_cat[i] * 10 + nz_vals[i]) % MOD
            pow10[i+1] = (pow10[i] * 10) % MOD
            
        ans = []
        for l, r in queries:
            start = bisect_left(nz_indices, l)
            end = bisect_right(nz_indices, r)
            
            if start >= end:
                ans.append(0)
                continue
            
            digit_sum = (pref_sum[end] - pref_sum[start]) % MOD
            length = end - start
            x = (pref_cat[end] - pref_cat[start] * pow10[length]) % MOD
            
            ans.append((x * digit_sum) % MOD)
            
        return ans