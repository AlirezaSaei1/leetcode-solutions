class Solution:
    def replaceDigits(self, s: str) -> str:
        ss = list(s)

        for i in range(1, len(ss), 2):
            ss[i] = chr(ord(ss[i-1]) + int(ss[i]))
        
        return ''.join(ss)
