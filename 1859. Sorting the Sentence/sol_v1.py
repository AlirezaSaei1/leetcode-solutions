class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        n = len(words)
        result = [''] * n

        for word in words:
            w, idx = word[:-1], word[-1]
            result[int(idx)-1] = w
        
        return ' '.join(result)