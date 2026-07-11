class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small = [0] * 26
        cap = [0] * 26

        for char in word:
            asc = ord(char)
            if 65 <= asc <= 90:
                cap[asc - 65] = 1
            
            if 97 <= asc <= 122:
                small[asc - 97] = 1
        
        return sum([a and b for a, b in zip(cap, small)])