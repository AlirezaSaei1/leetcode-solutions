class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        
        def has_b_square(target: int, hi: int) -> bool:
            lo = 1
            while lo <= hi:
                mid = (lo + hi) // 2
                sq = mid * mid
                if sq == target:
                    return True
                elif sq < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False
        
        for c in range(1, n + 1):
            cc = c * c
            for a in range(1, c):
                target = cc - a * a
                if target <= 0:
                    continue
                if has_b_square(target, c - 1):
                    ans += 1
        
        return ans
