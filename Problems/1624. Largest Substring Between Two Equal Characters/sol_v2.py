class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_pos = {}
        max_len = -1

        for i, ch in enumerate(s):
            if ch in first_pos:
                max_len = max(max_len, i - first_pos[ch] - 1)
            else:
                first_pos[ch] = i

        return max_len
