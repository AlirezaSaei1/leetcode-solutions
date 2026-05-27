class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small_mask = 0
        cap_mask = 0
        invalid_mask = 0
        
        for char in word:
            asc = ord(char)
            
            if 65 <= asc <= 90:
                bit = 1 << (asc - 65)
                cap_mask |= bit
                
            elif 97 <= asc <= 122:
                bit = 1 << (asc - 97)
                small_mask |= bit
                
                if cap_mask & bit:
                    invalid_mask |= bit
                    
        valid_mask = small_mask & cap_mask & ~invalid_mask
        return valid_mask.bit_count()