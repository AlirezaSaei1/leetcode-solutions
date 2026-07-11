class Solution:
    def checkString(self, s: str) -> bool:
        seenb = False
        for char in s:
            if char == 'a':
                if seenb:
                    return False
            else:
                seenb = True
        
        return True
