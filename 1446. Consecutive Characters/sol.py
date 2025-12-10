class Solution:
    def maxPower(self, s: str) -> int:
        max_sub = cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
                max_sub = max(max_sub, cur)
            else:
                cur = 1
        return max_sub

