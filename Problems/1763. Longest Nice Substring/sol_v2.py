class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(t: str) -> str:
            if len(t) < 2:
                return ""

            st = set(t)
            for i, ch in enumerate(t):
                if ch.swapcase() not in st:
                    left = solve(t[:i])
                    right = solve(t[i+1:])
                    return left if len(left) >= len(right) else right
            return t

        return solve(s)
