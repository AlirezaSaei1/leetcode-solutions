class Solution:
    def lexSmallest(self, s: str) -> str:
        if len(s) == 2:
            return min(s[0] + s[1], s[1] + s[0])
        strs = []

        for k in range(len(s)):
            strs.append(s[:k][::-1] + s[k:])
            strs.append(s[:-k] + s[-k::][::-1])

        return min(strs)