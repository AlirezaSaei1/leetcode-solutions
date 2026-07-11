class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask = 0
        for char in allowed:
            mask |= 1 << (ord(char) - 97)
            
        count = 0
        for word in words:
            for char in word:
                if not (mask & (1 << (ord(char) - 97))):
                    break
            else:
                count += 1
        return count