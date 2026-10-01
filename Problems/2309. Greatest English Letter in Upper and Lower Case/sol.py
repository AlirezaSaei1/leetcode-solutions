class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(s)
        
        for ch in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(ch)
            lower = upper.lower()
            if upper in seen and lower in seen:
                return upper
                
        return ""