class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            lena = len(a)
            lenb = len(b)
            return max(lena, lenb)