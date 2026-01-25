class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            chars = set(sub)
            for c in chars:
                if c.lower() not in chars or c.upper() not in chars:
                    return False
            return True

        n = len(s)
        max_len = 0
        answer = ''

        for i in range(n):
            for j in range(i + 1, n + 1):
                if is_nice(s[i:j]):
                    if j - i > max_len:
                        max_len = j - i
                        answer = s[i:j]

        return answer
