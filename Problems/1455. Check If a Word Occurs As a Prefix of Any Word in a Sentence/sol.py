class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        n = len(words)
        ns = len(searchWord)

        for i in range(n):
            if words[i].startswith(searchWord):
                return i + 1
        
        else:
            return -1