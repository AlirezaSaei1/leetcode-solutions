class Solution:
    def minTimeToType(self, word: str) -> int:
        total_seconds = len(word)
        cur = 'a'

        for char in word:
            dist = abs(ord(char) - ord(cur))
            total_seconds += min(dist, 26 - dist)
            cur = char
        
        return total_seconds