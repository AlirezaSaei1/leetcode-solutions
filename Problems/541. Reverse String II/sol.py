class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        counter = 1
        for i in range(0, len(s), k):
            if counter % 2 == 1:
                s = s[:i] + s[i:min(i+k, len(s))][::-1] + s[min(i+k, len(s)):]
            counter += 1
        
        return s

