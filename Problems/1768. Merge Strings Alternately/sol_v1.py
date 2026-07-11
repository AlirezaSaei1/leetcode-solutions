class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, w1 = len(word1), list(word1)
        n2, w2 = len(word2), list(word2)
        
        answer = []
        m = min(n1, n2)
        for i in range(m):
            answer.append(w1[i])
            answer.append(w2[i])
        
        if m == n1:
            answer.append(word2[m:])
        else:
            answer.append(word1[m:])
        
        return ''.join(answer)

        