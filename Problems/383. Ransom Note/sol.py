class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)

        for char in ransomNote:
            if ransom_count[char] > magazine_count[char]:
                return False
        
        return True