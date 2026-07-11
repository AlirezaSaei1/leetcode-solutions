class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        for char in string.ascii_lowercase:
            if abs(c1[char] - c2[char]) > 3:
                return False
                
        return True
