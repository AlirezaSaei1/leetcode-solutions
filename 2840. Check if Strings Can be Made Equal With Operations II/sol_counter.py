class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if Counter(s1[0::2]) != Counter(s2[0::2]):
            return False
            
        if Counter(s1[1::2]) != Counter(s2[1::2]):
            return False
            
        return True