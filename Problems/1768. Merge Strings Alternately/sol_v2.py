class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        out = []
        for i in range(m):
            out.append(word1[i])
            out.append(word2[i])
        out.append(word1[m:])
        out.append(word2[m:])
        return ''.join(out)
