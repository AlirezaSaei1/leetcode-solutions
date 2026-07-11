class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s).values()
        return len(freq) == 0 or min(freq) == max(freq)