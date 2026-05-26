class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small_mask = 0
        cap_mask = 0
        
        for char in word:
            asc = ord(char)
            if 65 <= asc <= 90:
                cap_mask |= (1 << (asc - 65))
            elif 97 <= asc <= 122:
                small_mask |= (1 << (asc - 97))
                
        return (small_mask & cap_mask).bit_count()