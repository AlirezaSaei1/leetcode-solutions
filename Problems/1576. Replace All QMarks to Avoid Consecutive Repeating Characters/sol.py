class Solution:
    def modifyString(self, s: str) -> str:
        sarr = list(s)
        n = len(sarr)

        for i in range(n):
            if sarr[i] == '?':
                left = sarr[i-1] if i > 0 else None
                right = sarr[i+1] if i < n-1 else None
                
                for ch in "abc":
                    if ch != left and ch != right:
                        sarr[i] = ch
                        break
        
        return ''.join(sarr)