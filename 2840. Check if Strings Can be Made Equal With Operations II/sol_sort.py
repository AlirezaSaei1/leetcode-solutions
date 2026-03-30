class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        evens1 = [s1[i] for i in range(n) if i % 2 == 0]
        evens2 = [s2[i] for i in range(n) if i % 2 == 0]
        odds1 = [s1[i] for i in range(n) if i % 2 == 1]
        odds2 = [s2[i] for i in range(n) if i % 2 == 1]
        
        return (sorted(evens1) == sorted(evens2)) and (sorted(odds1) == sorted(odds2))
        