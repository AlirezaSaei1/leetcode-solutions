class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s

        diff1 = diff2 = 0
        res = float('inf')

        for i in range(len(s)):
            if s[i] != '01'[i % 2]:
                diff1 += 1
            if s[i] != '10'[i % 2]:
                diff2 += 1

            if i >= n:
                if s[i-n] != '01'[(i-n) % 2]:
                    diff1 -= 1
                if s[i-n] != '10'[(i-n) % 2]:
                    diff2 -= 1

            if i >= n - 1:
                res = min(res, diff1, diff2)

        return res