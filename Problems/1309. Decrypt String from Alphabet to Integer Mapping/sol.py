class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        n = len(s) - 1

        while n >= 0:
            if s[n] == '#':
                num = s[n-2:n]
                n -= 3
            else:
                num = s[n]
                n -= 1
            
            ans.append(chr(ord('a') + int(num) - 1))
        
        return ''.join(ans[::-1])
