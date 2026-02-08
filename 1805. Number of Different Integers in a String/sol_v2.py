class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        cleaned = ''.join(c if c.isdigit() else ' ' for c in word)
        return len({int(x) for x in cleaned.split()})
