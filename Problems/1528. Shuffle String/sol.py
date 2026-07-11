class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [0] * n

        for i in range(n):
            result[indices[i]] = s[i]

        return ''.join(result)