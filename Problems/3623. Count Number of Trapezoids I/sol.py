class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        cnt = Counter()
        for x, y in points:
            cnt[y] += 1
        
        combos = []
        for c in cnt.values():
            if c >= 2:
                combos.append(c * (c - 1) // 2)

        if len(combos) < 2:
            return 0

        ans = 0
        prefix = 0
        for d in combos:
            ans = (ans + prefix * d) % MOD
            prefix = (prefix + d) % MOD
        
        return ans % MOD

