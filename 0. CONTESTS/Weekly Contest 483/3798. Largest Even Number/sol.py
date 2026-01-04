class Solution:
    def largestEven(self, s: str) -> str:
        n = len(s)
        for i in range(n):
            if s[~i] == '2':
                return s[:n-i]
        return ''