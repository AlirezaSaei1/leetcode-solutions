class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [0] * n
        char_code = 1
        
        for i in range(n):
            if res[i]: continue
            if char_code > 26: return ""
            
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = char_code
            char_code += 1
            
        word = "".join(chr(ord('a') + c - 1) for c in res)
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                current_lcp = 0
                if word[i] == word[j]:
                    if i + 1 < n and j + 1 < n:
                        current_lcp = 1 + lcp[i + 1][j + 1]
                    else:
                        current_lcp = 1
                
                if lcp[i][j] != current_lcp:
                    return ""
                    
        return word